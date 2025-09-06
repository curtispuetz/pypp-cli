#pragma once
#include <exception>
#include <py_str.h>

namespace pypp {
class PyppException : public std::exception {
  public:
    explicit PyppException(const PyStr &msg)
        : msg_(PyStr("PyppException: ") + msg) {}

    const char *what() const noexcept override { return msg_.str().c_str(); }

  protected:
    PyStr msg_;
};

class PyppNameError : public PyppException {
  public:
    explicit PyppNameError(const PyStr &msg)
        : PyppException(PyStr("PyppNameError: ") + msg) {}
};

class PyppImportError : public PyppException {
  public:
    explicit PyppImportError(const PyStr &msg)
        : PyppException(PyStr("PyppImportError: ") + msg) {}
};

class PyppStopIteration : public PyppException {
  public:
    explicit PyppStopIteration(const PyStr &msg = PyStr("Iteration stopped"))
        : PyppException(PyStr("PyppStopIteration: ") + msg) {}
};

} // namespace pypp
