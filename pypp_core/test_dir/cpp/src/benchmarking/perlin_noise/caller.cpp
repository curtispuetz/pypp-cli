#include "benchmarking\perlin_noise\caller.h"
#include "benchmarking/perlin_noise/impl.h"
#include "py_range.h"
#include "py_str.h"
#include "pypp_random.h"
#include "pypp_time.h"
#include "pypp_util/print.h"

void perlin_noise_fn() {
    print(PyStr("PERLIN NOISE RESULTS:"));
    random::Random rng = random::Random(42);
    PerlinNoise p = create_perlin_noise(512, rng);
    auto a = pypp_time::perf_counter_start();
    for (int i = 0; i < 1000000; i += 1) {
        double shift = i * 1e-05;
        p.calc(0.7 + shift, 0.6 + shift, 1, 0.5, 2.0);
    }
    double b = pypp_time::perf_counter_end(a);
    print(PyStr(std::format("Time taken: {} seconds", b)));
}
