// GPU kernels and wrappers for shared state methods.

#include <cstdint>

#include <backends/event.hpp>
#include <backends/multi_event_stream_state.hpp>

#include <arbor/gpu/gpu_api.hpp>
#include <arbor/gpu/gpu_common.hpp>

namespace arb {
namespace gpu {

namespace kernel {

template <typename T>
__global__ void update_time_to_impl(unsigned n,
                                    T* __restrict__ const time_to,
                                    const T* __restrict__ const time,
                                    T dt,
                                    T tmax) {
    unsigned i = threadIdx.x+blockIdx.x*blockDim.x;
    if (i<n) {
        auto t = time[i]+dt;
        time_to[i] = t<tmax? t: tmax;
    }
}

// Vector/scalar addition: x[i] += v ∀i
template <typename T>
__global__ void add_scalar(unsigned n,
                           T* __restrict__ const x,
                           arb_value_type v) {
    unsigned i = threadIdx.x+blockIdx.x*blockDim.x;
    if (i<n) {
        x[i] += v;
    }
}

template <typename T, typename I>
__global__ void set_dt_impl(      T* __restrict__ dt_intdom,
                            const T* __restrict__ time_to,
                            const T* __restrict__ time,
                            const unsigned ncomp,
                                  T* __restrict__ dt_comp,
                            const I* __restrict__ cv_to_intdom) {
    auto idx = blockIdx.x*blockDim.x + threadIdx.x;
    if (idx < ncomp) {
        const auto ind = cv_to_intdom[idx];
        const auto dt = time_to[ind] - time[ind];
        dt_intdom[ind] = dt;
        dt_comp[idx] = dt;
    }
}

__global__ void take_samples_impl(
    multi_event_stream_state<raw_probe_info> s,
    const arb_value_type* __restrict__ const time,
    arb_value_type* __restrict__ const sample_time,
    arb_value_type* __restrict__ const sample_value)
{
    unsigned i = threadIdx.x+blockIdx.x*blockDim.x;
    if (i<s.n) {
        auto begin = s.ev_data+s.begin_offset[i];
        auto end = s.ev_data+s.end_offset[i];
        for (auto p = begin; p!=end; ++p) {
            sample_time[p->offset] = time[i];
            sample_value[p->offset] = p->handle? *p->handle: 0;
        }
    }
}

} // namespace kernel

using impl::block_count;

void add_scalar(std::size_t n, arb_value_type* data, arb_value_type v) {
    if (!n) return;

    constexpr int block_dim = 128;
    const int nblock = block_count(n, block_dim);
    kernel::add_scalar<<<nblock, block_dim>>>(n, data, v);
}

void update_time_to_impl(
    std::size_t n, arb_value_type* time_to, const arb_value_type* time,
    arb_value_type dt, arb_value_type tmax)
{
    if (!n) return;

    constexpr int block_dim = 128;
    const int nblock = block_count(n, block_dim);
    kernel::update_time_to_impl<<<nblock, block_dim>>>(n, time_to, time, dt, tmax);
}

void set_dt_impl(
    arb_size_type nintdom, arb_size_type ncomp, arb_value_type* dt_intdom, arb_value_type* dt_comp,
    const arb_value_type* time_to, const arb_value_type* time, const arb_index_type* cv_to_intdom)
{
    if (!nintdom || !ncomp) return;

    constexpr int block_dim = 128;
    const int nblock = block_count(ncomp, block_dim);
    kernel::set_dt_impl<<<nblock, block_dim>>>(dt_intdom, time_to, time, ncomp, dt_comp, cv_to_intdom);
}

void take_samples_impl(
    const multi_event_stream_state<raw_probe_info>& s,
    const arb_value_type* time, arb_value_type* sample_time, arb_value_type* sample_value)
{
    if (!s.n_streams()) return;

    constexpr int block_dim = 128;
    const int nblock = block_count(s.n_streams(), block_dim);
    kernel::take_samples_impl<<<nblock, block_dim>>>(s, time, sample_time, sample_value);
}

} // namespace gpu
} // namespace arb
