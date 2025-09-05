#pragma once

#include <stdexcept>
class PyStr;

class PyppRuntimeError : public std::runtime_error {
  public:
    PyppRuntimeError(const PyStr &msg);
    PyppRuntimeError(const std::string &msg);
};

class PyppValueError : public std::invalid_argument {
  public:
    PyppValueError(const PyStr &msg);
    PyppValueError(const std::string &msg);
};

class PyppTypeError : public std::invalid_argument {
  public:
    PyppTypeError(const PyStr &msg);
    PyppTypeError(const std::string &msg);
};

class PyppIndexError : public std::out_of_range {
  public:
    PyppIndexError(const PyStr &msg);
    PyppIndexError(const std::string &msg);
};

class PyppKeyError : public std::out_of_range {
  public:
    PyppKeyError(const PyStr &msg);
    PyppKeyError(const std::string &msg);
};

class PyppZeroDivisionError : public std::domain_error {
  public:
    PyppZeroDivisionError(const PyStr &msg);
    PyppZeroDivisionError(const std::string &msg);
};

class PyppAssertionError : public std::logic_error {
  public:
    PyppAssertionError(const PyStr &msg);
    PyppAssertionError(const std::string &msg);
};

class PyppNotImplementedError : public std::logic_error {
  public:
    PyppNotImplementedError(const PyStr &msg);
    PyppNotImplementedError(const std::string &msg);
};

class PyppAttributeError : public std::logic_error {
  public:
    PyppAttributeError(const PyStr &msg);
    PyppAttributeError(const std::string &msg);
};
