#pragma once

#include "exceptions/exception.h"

namespace pypp {
class PyStr;
class ValueError : public Exception {
  public:
    ValueError(const PyStr &msg);
    ValueError(const std::string &msg);
};

class AssertionError : public Exception {
  public:
    AssertionError(const PyStr &msg);
};
class LookupError : public Exception {
  public:
    LookupError(const PyStr &msg);
};

class IndexError : public LookupError {
  public:
    IndexError(const PyStr &msg);
    IndexError(const std::string &msg);
};

class KeyError : public LookupError {
  public:
    KeyError(const PyStr &msg);
    KeyError(const std::string &msg);
};
class RuntimeError : public Exception {
  public:
    RuntimeError(const PyStr &msg);
    RuntimeError(const std::string &msg);
};

class NotImplementedError : public RuntimeError {
  public:
    NotImplementedError(const PyStr &msg);
};

} // namespace pypp