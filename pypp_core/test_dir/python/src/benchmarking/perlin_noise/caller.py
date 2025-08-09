import random

from benchmarking.perlin_noise.impl import PerlinNoise, create_perlin_noise


# TODO: stop ignoring this and test it.
def perlin_noise_fn():
    rng: random.Random = random.Random(42)
    p: PerlinNoise = create_perlin_noise(512, rng)
    print(p.calc(0.5, 0.5))
