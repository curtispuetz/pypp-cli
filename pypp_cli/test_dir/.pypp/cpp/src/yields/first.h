#pragma once

#include "pypp_util/generator.h"

namespace me {
pypp::Generator<int> yield_123();
pypp::Generator<int> yield_over_list();
pypp::Generator<int> yield_from_example();
void yield_fn();
} // namespace me