#pragma once

#include "py_list.h"
#include <algorithm>
#include <exceptions/common.h>
#include <random>
#include <vector>

namespace pypp {
namespace random {

class Random {
  public:
    Random(int seed_val = std::random_device{}());
    void seed(int s);
    double random();
    int randint(int a, int b);
    template <typename T> void shuffle(PyList<T> &v);
    template <typename T> T choice(const PyList<T> &v);

  private:
    std::mt19937 rng;
    std::uniform_real_distribution<double> dist_real{0.0, 1.0};
};

template <typename T> void Random::shuffle(PyList<T> &v) {
    std::shuffle(v.begin(), v.end(), rng);
}

template <typename T> T Random::choice(const PyList<T> &v) {
    if (v.len() == 0)
        throw IndexError("Cannot choose from an empty sequence");
    std::uniform_int_distribution<size_t> dist(0, v.len() - 1);
    return v[dist(rng)];
}

} // namespace random
} // namespace pypp