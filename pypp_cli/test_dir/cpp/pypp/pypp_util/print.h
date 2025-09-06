#pragma once

#include <iostream>

namespace pypp {

template <typename... Args> void print(const Args &...args) {
    ((std::cout << args << ' '), ...) << std::endl;
}

} // namespace pypp