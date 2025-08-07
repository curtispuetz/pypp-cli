#pragma once
#include <exception>
#include <string>

class PyppException : public std::exception {
  public:
    explicit PyppException(const std::string &msg)
        : msg_("PyppException: " + msg) {}

    const char *what() const noexcept override { return msg_.c_str(); }

  protected:
    std::string msg_;
};

class PyppNameError : public PyppException {
  public:
    explicit PyppNameError(const std::string &msg)
        : PyppException("PyppNameError: " + msg) {}
};

class PyppImportError : public PyppException {
  public:
    explicit PyppImportError(const std::string &msg)
        : PyppException("PyppImportError: " + msg) {}
};

class PyppStopIteration : public PyppException {
  public:
    explicit PyppStopIteration(const std::string &msg = "Iteration stopped")
        : PyppException("PyppStopIteration: " + msg) {}
};
