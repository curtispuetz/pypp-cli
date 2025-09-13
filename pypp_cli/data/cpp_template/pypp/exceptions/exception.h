#pragma once
#include <exception>
#include <py_str.h>

namespace pypp {
class Exception : public std::exception {
  public:
    explicit Exception(const PyStr &msg) : msg_(PyStr("Exception: ") + msg) {}

    const char *what() const noexcept override { return msg_.str().c_str(); }

  protected:
    PyStr msg_;
};

class NameError : public Exception {
  public:
    explicit NameError(const PyStr &msg)
        : Exception(PyStr("NameError: ") + msg) {}
};

class ImportError : public Exception {
  public:
    explicit ImportError(const PyStr &msg)
        : Exception(PyStr("ImportError: ") + msg) {}
};

class StopIteration : public Exception {
  public:
    explicit StopIteration(const PyStr &msg = PyStr("Iteration stopped"))
        : Exception(PyStr("StopIteration: ") + msg) {}
};

} // namespace pypp
