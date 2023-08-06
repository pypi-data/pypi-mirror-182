#pragma once

#include <cmath>
#include <iosfwd>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

#include <arbor/export.hpp>
#include <arbor/assert.hpp>
#include <arbor/common_types.hpp>
#include <arbor/fvm_types.hpp>
#include <arbor/simd/simd.hpp>

#include "backends/event.hpp"
#include "backends/rand_fwd.hpp"
#include "util/padded_alloc.hpp"
#include "util/rangeutil.hpp"

#include "multi_event_stream.hpp"
#include "threshold_watcher.hpp"
#include "fvm_layout.hpp"
#include "multicore_common.hpp"
#include "partition_by_constraint.hpp"
#include "backends/multicore/cable_solver.hpp"
#include "backends/multicore/diffusion_solver.hpp"

namespace arb {
namespace multicore {

/*
 * Ion state fields correspond to NMODL ion variables, where X
 * is replaced with the name of the ion. E.g. for calcium 'ca':
 *
 *     Field   NMODL variable   Meaning
 *     -------------------------------------------------------
 *     iX_     ica              calcium ion current density
 *     eX_     eca              calcium ion channel reversal potential
 *     Xi_     cai              internal calcium concentration
 *     Xo_     cao              external calcium concentration
 */
struct ARB_ARBOR_API ion_state {
    using solver_type = diffusion_solver;
    using solver_ptr  = std::unique_ptr<solver_type>;

    unsigned alignment = 1; // Alignment and padding multiple.

    bool write_eX_;          // is eX written?
    bool write_Xo_;          // is Xo written?
    bool write_Xi_;          // is Xi written?

    iarray node_index_;     // Instance to CV map.
    array iX_;              // (A/m²)  current density
    array eX_;              // (mV)    reversal potential
    array Xi_;              // (mM)    internal concentration
    array Xd_;              // (mM)    diffusive internal concentration
    array Xo_;              // (mM)    external concentration
    array gX_;              // (kS/m²) per-species conductivity

    array init_Xi_;         // (mM) area-weighted initial internal concentration
    array init_Xo_;         // (mM) area-weighted initial external concentration
    array reset_Xi_;        // (mM) area-weighted user-set internal concentration
    array reset_Xo_;        // (mM) area-weighted user-set internal concentration
    array init_eX_;         // (mV) initial reversal potential

    array charge;           // charge of ionic species (global value, length 1)

    solver_ptr solver = nullptr;

    ion_state() = default;

    ion_state(
        int charge,
        const fvm_ion_config& ion_data,
        unsigned align,
        solver_ptr ptr
    );

    // Set ion concentrations to weighted proportion of default concentrations.
    void init_concentration();

    // Set ionic current density to zero.
    void zero_current();

    // Zero currents, reset concentrations, and reset reversal potential from initial values.
    void reset();
};

struct ARB_ARBOR_API istim_state {
    unsigned alignment = 1; // Alignment and padding multiple.

    // Immutable data (post initialization):
    iarray accu_index_;     // Instance to accumulator index (accu_stim_ index) map.
    iarray accu_to_cv_;     // Accumulator index to CV map.

    array frequency_;       // (kHz) stimulus frequency per instance.
    array phase_;           // (rad) stimulus waveform phase at t=0.
    array envl_amplitudes_; // (A/m²) stimulus envelope amplitudes, partitioned by instance.
    array envl_times_;      // (A/m²) stimulus envelope timepoints, partitioned by instance.
    iarray envl_divs_;      // Partition divisions for envl_ arrays,

    // Mutable data:
    array accu_stim_;       // (A/m²) accumulated stim current / CV area, one per CV with a stimulus.
    iarray envl_index_;     // Per instance index into envl_ arrays, corresponding to last sample time.

    // Zero stim current.
    void zero_current();

    // Zero stim current, reset indices.
    void reset();

    // Contribute to current density:
    void add_current(const array& time, const iarray& cv_to_intdom, array& current_density);

    // Construct state from i_clamp data:
    istim_state(const fvm_stimulus_config& stim_data, unsigned align);

    istim_state() = default;
};

struct ARB_ARBOR_API shared_state {
    struct mech_storage {
        array data_;
        iarray indices_;
        std::size_t value_width_padded;
        constraint_partition constraints_;
        std::vector<arb_value_type>  globals_;
        std::vector<arb_value_type*> parameters_;
        std::vector<arb_value_type*> state_vars_;
        std::vector<arb_ion_state>   ion_states_;

        std::array<std::vector<arb_value_type*>, cbprng::cache_size()> random_numbers_;
        std::vector<arb_size_type> gid_;
        std::vector<arb_size_type> idx_;
        cbprng::counter_type random_number_update_counter_ = 0u;
    };

    cable_solver solver;

    unsigned alignment = 1;   // Alignment and padding multiple.
    util::padded_allocator<> alloc;  // Allocator with corresponging alignment/padding.

    arb_size_type n_intdom = 0; // Number of integration domains.
    arb_size_type n_detector = 0; // Max number of detectors on all cells.
    arb_size_type n_cv = 0;   // Total number of CVs.

    iarray cv_to_intdom;      // Maps CV index to integration domain index.
    iarray cv_to_cell;        // Maps CV index to the first spike
    array time;               // Maps intdom index to integration start time [ms].
    array time_to;            // Maps intdom index to integration stop time [ms].
    array dt_intdom;          // Maps  index to (stop time) - (start time) [ms].
    array dt_cv;              // Maps CV index to dt [ms].
    array voltage;            // Maps CV index to membrane voltage [mV].
    array current_density;    // Maps CV index to membrane current density contributions [A/m²].
    array conductivity;       // Maps CV index to membrane conductivity [kS/m²].

    array init_voltage;       // Maps CV index to initial membrane voltage [mV].
    array temperature_degC;   // Maps CV to local temperature (read only) [°C].
    array diam_um;            // Maps CV to local diameter (read only) [µm].

    array time_since_spike;   // Stores time since last spike on any detector, organized by cell.
    iarray src_to_spike;      // Maps spike source index to spike index

    arb_seed_type cbprng_seed; // random number generator seed

    istim_state stim_data;
    std::unordered_map<std::string, ion_state> ion_data;
    deliverable_event_stream deliverable_events;
    std::unordered_map<unsigned, mech_storage> storage;

    shared_state() = default;

    shared_state(
        arb_size_type n_intdom,
        arb_size_type n_cell,
        arb_size_type n_detector,
        const std::vector<arb_index_type>& cv_to_intdom_vec,
        const std::vector<arb_index_type>& cv_to_cell_vec,
        const std::vector<arb_value_type>& init_membrane_potential,
        const std::vector<arb_value_type>& temperature_K,
        const std::vector<arb_value_type>& diam,
        const std::vector<arb_index_type>& src_to_spike,
        unsigned align,
        arb_seed_type cbprng_seed_ = 0u
    );

    void instantiate(mechanism&,
                     unsigned,
                     const mechanism_overrides&,
                     const mechanism_layout&,
                     const std::vector<std::pair<std::string, std::vector<arb_value_type>>>&);

    void update_prng_state(mechanism&);

    const arb_value_type* mechanism_state_data(const mechanism&, const std::string&);

    void add_ion(
        const std::string& ion_name,
        int charge,
        const fvm_ion_config& ion_data,
        ion_state::solver_ptr solver=nullptr);

    void configure_stimulus(const fvm_stimulus_config&);

    void zero_currents();

    void ions_init_concentration();

    void ions_nernst_reversal_potential(arb_value_type temperature_K);

    // Set time_to to earliest of time+dt_step and tmax.
    void update_time_to(arb_value_type dt_step, arb_value_type tmax);

    // Set the per-integration domain and per-compartment dt from time_to - time.
    void set_dt();

    // Update stimulus state and add current contributions.
    void add_stimulus_current();

    // Integrate by matrix solve.
    void integrate_voltage();
    void integrate_diffusion();

    // Return minimum and maximum time value [ms] across cells.
    std::pair<arb_value_type, arb_value_type> time_bounds() const;

    // Return minimum and maximum voltage value [mV] across cells.
    // (Used for solution bounds checking.)
    std::pair<arb_value_type, arb_value_type> voltage_bounds() const;

    // Take samples according to marked events in a sample_event_stream.
    void take_samples(
        const sample_event_stream::state& s,
        array& sample_time,
        array& sample_value);

    void reset();
};

// For debugging only:
ARB_ARBOR_API std::ostream& operator<<(std::ostream& o, const shared_state& s);


} // namespace multicore
} // namespace arb
