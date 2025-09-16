#include "src/benchmarking/perlin_noise/caller.h"
#include "py_str.h"
#include "pypp_random.h"
#include "pypp_time.h"
#include "pypp_util/print.h"
#include "src/benchmarking/perlin_noise/impl.h"

namespace me {
void perlin_noise_fn() {
    pypp::print(pypp::PyStr("PERLIN NOISE RESULTS:"));
    pypp::random::Random rng = pypp::random::Random(42);
    me::PerlinNoise p = me::create_perlin_noise(512, rng);
    auto a = pypp::time::perf_counter_start();
    for (int i = 0; i < 1000000; i += 1) {
        double shift = i * 1e-05;
        p.calc(0.7 + shift, 0.6 + shift, 1, 0.5, 2.0);
    }
    double b = pypp::time::perf_counter_end(a);
    pypp::print(pypp::PyStr(std::format("Time taken: {} seconds", b)));
}

} // namespace me