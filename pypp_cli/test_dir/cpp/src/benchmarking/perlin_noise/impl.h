#pragma once

#include "py_list.h"
#include "py_tuple.h"
#include "pypp_random.h"
#include <utility>

namespace me {
inline const pypp::PyList<pypp::PyTup<int, int>>
    GRADIENTS({pypp::PyTup(1, 0), pypp::PyTup(-1, 0), pypp::PyTup(0, 1),
               pypp::PyTup(0, -1), pypp::PyTup(1, 1), pypp::PyTup(-1, 1),
               pypp::PyTup(1, -1), pypp::PyTup(-1, -1)});
class PerlinNoise {
  public:
    int _p_len;
    pypp::PyList<int> _p;
    PerlinNoise(int a_permutation_table_size, pypp::PyList<int> a_permuted_list)
        : _p_len(std::move(a_permutation_table_size)),
          _p(std::move(a_permuted_list)) {}
    double calc(double x, double y, int octaves, double persistence,
                double lacunarity);
    double _calc_one_octave(double x, double y);
    int _hash(int x, int y);
    pypp::PyTup<int, int> _gradient_vector(int x, int y);
    pypp::PyTup<pypp::PyTup<int, int>, pypp::PyTup<int, int>,
                pypp::PyTup<int, int>, pypp::PyTup<int, int>, double, double>
    _calc_grad_vecs_and_relative_position(double x, double y);
};

PerlinNoise create_perlin_noise(int permutation_table_size,
                                pypp::random::Random &rng);
} // namespace me