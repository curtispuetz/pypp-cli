#include "pypp_random.h"

namespace pypp {
namespace random {

Random::Random(int seed_val)
    : rng(static_cast<unsigned int>(std::abs(seed_val))) {}

void Random::seed(int s) { rng.seed(static_cast<unsigned int>(std::abs(s))); }

double Random::random() { return dist_real(rng); }

int Random::randint(int a, int b) {
    std::uniform_int_distribution<int> dist(a, b);
    return dist(rng);
}

} // namespace random
} // namespace pypp