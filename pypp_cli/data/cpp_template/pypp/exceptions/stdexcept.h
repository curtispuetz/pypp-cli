#pragma once

#include <stdexcept>

namespace pypp {
class PyStr;
class RuntimeError : public std::runtime_error {
  public:
    RuntimeError(const PyStr &msg);
    RuntimeError(const std::string &msg);
};

class ValueError : public std::invalid_argument {
  public:
    ValueError(const PyStr &msg);
    ValueError(const std::string &msg);
};

class TypeError : public std::invalid_argument {
  public:
    TypeError(const PyStr &msg);
    TypeError(const std::string &msg);
};

class IndexError : public std::out_of_range {
  public:
    IndexError(const PyStr &msg);
    IndexError(const std::string &msg);
};

class KeyError : public std::out_of_range {
  public:
    KeyError(const PyStr &msg);
    KeyError(const std::string &msg);
};

class ZeroDivisionError : public std::domain_error {
  public:
    ZeroDivisionError(const PyStr &msg);
    ZeroDivisionError(const std::string &msg);
};

class AssertionError : public std::logic_error {
  public:
    AssertionError(const PyStr &msg);
    AssertionError(const std::string &msg);
};

class NotImplementedError : public std::logic_error {
  public:
    NotImplementedError(const PyStr &msg);
    NotImplementedError(const std::string &msg);
};

class AttributeError : public std::logic_error {
  public:
    AttributeError(const PyStr &msg);
    AttributeError(const std::string &msg);
};
} // namespace pypp