#include "benchmarking/perlin_noise/impl.h"
#include "py_range.h"
#include <cmath>

double _fade(double t) { return ((t * t) * t) * ((t * ((t * 6) - 15)) + 10); }

double _lerp(double t, double y_1, double y_2) {
    return y_1 + (t * (y_2 - y_1));
}

double PerlinNoise::calc(double x, double y, int octaves, double persistence,
                         double lacunarity) {
    double freq = 1.0;
    double amplitude = 1.0;
    double noise = 0.0;
    for (int _ = 0; _ < octaves; _ += 1) {
        noise += _calc_one_octave(x * freq, y * freq) * amplitude;
        amplitude *= persistence;
        freq *= lacunarity;
    }
    return noise;
}

double PerlinNoise::_calc_one_octave(double x, double y) {
    auto [g00, g10, g01, g11, u, v] =
        _calc_grad_vecs_and_relative_position(x, y);
    double s = _fade(u);
    double t = _fade(v);
    double dot1 = (g00.get<0>() * u) + (g00.get<1>() * v);
    double dot2 = (g10.get<0>() * (u - 1)) + (g10.get<1>() * v);
    double dot3 = (g01.get<0>() * u) + (g01.get<1>() * (v - 1));
    double dot4 = (g11.get<0>() * (u - 1)) + (g11.get<1>() * (v - 1));
    double i1 = _lerp(s, dot1, dot2);
    double i2 = _lerp(s, dot3, dot4);
    return _lerp(t, i1, i2);
}

int PerlinNoise::_hash(int x, int y) {
    return _p[(_p[x % _p_len] + y) % _p_len];
}

PyTup<int, int> PerlinNoise::_gradient_vector(int x, int y) {
    int i = _hash(x, y) % 8;
    return GRADIENTS[i];
}

PyTup<PyTup<int, int>, PyTup<int, int>, PyTup<int, int>, PyTup<int, int>,
      double, double>
PerlinNoise::_calc_grad_vecs_and_relative_position(double x, double y) {
    int x0 = int(std::floor(x));
    int y0 = int(std::floor(y));
    int x1 = x0 + 1;
    int y1 = y0 + 1;
    double u = x - x0;
    double v = y - y0;
    return PyTup(_gradient_vector(x0, y0), _gradient_vector(x1, y0),
                 _gradient_vector(x0, y1), _gradient_vector(x1, y1), u, v);
}

PerlinNoise create_perlin_noise(int permutation_table_size,
                                random::Random &rng) {
    PyList<int> arr_to_shuffle;
    for (int i = 1; i < permutation_table_size + 1; i += 1) {
        arr_to_shuffle.append(std::move(i));
    }
    rng.shuffle(arr_to_shuffle);
    return PerlinNoise(permutation_table_size, std::move(arr_to_shuffle));
}
