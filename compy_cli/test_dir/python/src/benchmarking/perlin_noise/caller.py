import random

from compy_python.custom_types import auto
import compy_python.stl.compy_time as compy_time

from benchmarking.perlin_noise.impl import PerlinNoise, create_perlin_noise


def perlin_noise_fn():
    print("PERLIN NOISE RESULTS:")
    rng: random.Random = random.Random(42)
    p: PerlinNoise = create_perlin_noise(512, rng)
    a: auto = compy_time.perf_counter_start()
    for i in range(1000000):
        shift: float = i * 0.00001
        p.calc(0.7 + shift, 0.6 + shift, 1, 0.5, 2.0)
    b: float = compy_time.perf_counter_end(a)
    # Transpiled C++ is about 45 times faster than python run
    print(f"Time taken: {b} seconds")
