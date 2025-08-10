#pragma once
#include "py_list.h"
#include <algorithm>
#include <random>
#include <stdexcept>
#include <vector>

namespace random {

class Random {
  public:
    Random(int seed_val = std::random_device{}());
    void seed(int s);

    // Equivalent to random() in Python: float in [0.0, 1.0)
    double random();

    // Equivalent to randint(a, b) in Python: int in [a, b]
    int randint(int a, int b);

    // Equivalent to shuffle in Python (in-place)
    template <typename T> void shuffle(PyList<T> &v);

    // Equivalent to choice in Python: pick a random element
    template <typename T> T choice(const PyList<T> &v);

  private:
    std::mt19937 rng;
    std::uniform_real_distribution<double> dist_real{0.0, 1.0};
};

// --- Template implementations ---

template <typename T> void Random::shuffle(PyList<T> &v) {
    std::shuffle(v.begin(), v.end(), rng);
}

template <typename T> T Random::choice(const PyList<T> &v) {
    if (v.len() == 0)
        throw std::runtime_error("Cannot choose from empty list");
    std::uniform_int_distribution<size_t> dist(0, v.len() - 1);
    return v[dist(rng)];
}

} // namespace random