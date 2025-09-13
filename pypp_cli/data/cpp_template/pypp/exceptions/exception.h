#pragma once

#include <string>

// TODO later: I think I should just not inherit from std::exception, because
// then I don't need to define the what() method. Then In my code, I should
// catch all exceptions and throw my own exceptions
namespace pypp {
class PyStr;
class Exception {
  public:
    explicit Exception(const PyStr &msg);
    const char *what() const noexcept;

  protected:
    std::string msg_;
};
} // namespace pypp
