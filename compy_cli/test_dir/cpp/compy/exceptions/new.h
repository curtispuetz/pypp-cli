#pragma once
#include <new>

class CompyMemoryError : public std::bad_alloc {
  public:
    const char *what() const noexcept override {
        return "CompyMemoryError: failed to allocate memory";
    }
};
