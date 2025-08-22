#pragma once
#include <stdexcept>
#include <string>

class PyppRuntimeError : public std::runtime_error {
  public:
    explicit PyppRuntimeError(const std::string &msg)
        : std::runtime_error("PyppRuntimeError: " + msg) {}
};

class PyppValueError : public std::invalid_argument {
  public:
    explicit PyppValueError(const std::string &msg)
        : std::invalid_argument("PyppValueError: " + msg) {}
};

class PyppTypeError : public std::invalid_argument {
  public:
    explicit PyppTypeError(const std::string &msg)
        : std::invalid_argument("PyppTypeError: " + msg) {}
};

class PyppIndexError : public std::out_of_range {
  public:
    explicit PyppIndexError(const std::string &msg)
        : std::out_of_range("PyppIndexError: " + msg) {}
};

class PyppKeyError : public std::out_of_range {
  public:
    explicit PyppKeyError(const std::string &msg)
        : std::out_of_range("PyppKeyError: " + msg) {}
};

// This is not used and zero division will do indefined behavior in the C++
// execution?
class PyppZeroDivisionError : public std::domain_error {
  public:
    explicit PyppZeroDivisionError(const std::string &msg)
        : std::domain_error("PyppZeroDivisionError: " + msg) {}
};

class PyppAssertionError : public std::logic_error {
  public:
    explicit PyppAssertionError(const std::string &msg)
        : std::logic_error("PyppAssertionError: " + msg) {}
};

class PyppNotImplementedError : public std::logic_error {
  public:
    explicit PyppNotImplementedError(const std::string &msg)
        : std::logic_error("PyppNotImplementedError: " + msg) {}
};

class PyppAttributeError : public std::logic_error {
  public:
    explicit PyppAttributeError(const std::string &msg)
        : std::logic_error("PyppAttributeError: " + msg) {}
};
