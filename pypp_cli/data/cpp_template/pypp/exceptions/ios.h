#pragma once
#include <ios>
#include <string>

namespace pypp {
class PyStr;
class IOError : public std::ios_base::failure {
  public:
    IOError(const PyStr &msg);
    IOError(const std::string &msg);
};
} // namespace pypp
