#pragma once
#include <new>

namespace pypp {
class MemoryError : public std::bad_alloc {
  public:
    const char *what() const noexcept override {
        return "MemoryError: failed to allocate memory";
    }
};

} // namespace pypp
