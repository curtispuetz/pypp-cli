#pragma once
#include <string>
#include <system_error>

namespace pypp {
class PyStr;
class OSError : public std::system_error {
  public:
    OSError(const PyStr &msg, std::error_code ec);
    OSError(const std::string &msg, std::error_code ec);
};

class SystemError : public std::system_error {
  public:
    SystemError(const PyStr &msg, std::error_code ec);
    SystemError(const std::string &msg, std::error_code ec);
};
} // namespace pypp