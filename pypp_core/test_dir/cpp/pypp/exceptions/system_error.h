#pragma once
#include <string>
#include <system_error>

class PyppOSError : public std::system_error {
  public:
    PyppOSError(const std::string &msg, std::error_code ec)
        : std::system_error(ec, "PyppOsError: " + msg) {}
};

class PyppSystemError : public std::system_error {
  public:
    PyppSystemError(const std::string &msg, std::error_code ec)
        : std::system_error(ec, "PyppSystemError: " + msg) {}
};