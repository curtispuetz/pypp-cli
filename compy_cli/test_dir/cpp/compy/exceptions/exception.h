#pragma once
#include <exception>
#include <string>

class CompyException : public std::exception {
  public:
    explicit CompyException(const std::string &msg)
        : msg_("CompyException: " + msg) {}

    const char *what() const noexcept override { return msg_.c_str(); }

  protected:
    std::string msg_;
};

class CompyNameError : public CompyException {
  public:
    explicit CompyNameError(const std::string &msg)
        : CompyException("CompyNameError: " + msg) {}
};

class CompyImportError : public CompyException {
  public:
    explicit CompyImportError(const std::string &msg)
        : CompyException("CompyImportError: " + msg) {}
};

class CompyStopIteration : public CompyException {
  public:
    explicit CompyStopIteration(const std::string &msg = "Iteration stopped")
        : CompyException("CompyStopIteration: " + msg) {}
};
