#pragma once
#include <stdexcept>
#include <string>

class CompyRuntimeError : public std::runtime_error {
  public:
    explicit CompyRuntimeError(const std::string &msg)
        : std::runtime_error("CompyRuntimeError: " + msg) {}
};

class CompyValueError : public std::invalid_argument {
  public:
    explicit CompyValueError(const std::string &msg)
        : std::invalid_argument("CompyValueError: " + msg) {}
};

class CompyTypeError : public std::invalid_argument {
  public:
    explicit CompyTypeError(const std::string &msg)
        : std::invalid_argument("CompyTypeError: " + msg) {}
};

class CompyIndexError : public std::out_of_range {
  public:
    explicit CompyIndexError(const std::string &msg)
        : std::out_of_range("CompyIndexError: " + msg) {}
};

class CompyKeyError : public std::out_of_range {
  public:
    explicit CompyKeyError(const std::string &msg)
        : std::out_of_range("CompyKeyError: " + msg) {}
};

// This is not used and zero division will do indefined behavior in the C++
// execution?
class CompyZeroDivisionError : public std::domain_error {
  public:
    explicit CompyZeroDivisionError(const std::string &msg)
        : std::domain_error("CompyZeroDivisionError: " + msg) {}
};

class CompyAssertionError : public std::logic_error {
  public:
    explicit CompyAssertionError(const std::string &msg)
        : std::logic_error("CompyAssertionError: " + msg) {}
};

class CompyNotImplementedError : public std::logic_error {
  public:
    explicit CompyNotImplementedError(const std::string &msg)
        : std::logic_error("CompyNotImplementedError: " + msg) {}
};

class CompyAttributeError : public std::logic_error {
  public:
    explicit CompyAttributeError(const std::string &msg)
        : std::logic_error("CompyAttributeError: " + msg) {}
};
