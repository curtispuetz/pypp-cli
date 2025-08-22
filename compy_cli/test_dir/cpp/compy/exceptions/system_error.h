#pragma once
#include <string>
#include <system_error>

class CompyOSError : public std::system_error {
  public:
    CompyOSError(const std::string &msg, std::error_code ec)
        : std::system_error(ec, "CompyOsError: " + msg) {}
};

class CompySystemError : public std::system_error {
  public:
    CompySystemError(const std::string &msg, std::error_code ec)
        : std::system_error(ec, "CompySystemError: " + msg) {}
};