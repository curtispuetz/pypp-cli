#pragma once
#include <string>
#include <system_error>

class PyStr;

class PyppOSError : public std::system_error {
  public:
    PyppOSError(const PyStr &msg, std::error_code ec);
    PyppOSError(const std::string &msg, std::error_code ec);
};

class PyppSystemError : public std::system_error {
  public:
    PyppSystemError(const PyStr &msg, std::error_code ec);
    PyppSystemError(const std::string &msg, std::error_code ec);
};