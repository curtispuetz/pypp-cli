#pragma once
#include <new>

namespace pypp {
class PyppMemoryError : public std::bad_alloc {
  public:
    const char *what() const noexcept override {
        return "PyppMemoryError: failed to allocate memory";
    }
};

} // namespace pypp
