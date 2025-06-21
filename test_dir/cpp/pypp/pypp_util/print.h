#pragma once

#include <iostream>

template <typename... Args> void print(const Args &...args) {
    ((std::cout << args << ' '), ...) << std::endl;
}