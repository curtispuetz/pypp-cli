#pragma once
#include <ios>
#include <string>

namespace pypp {
class PyStr;
class PyppIOError : public std::ios_base::failure {
  public:
    PyppIOError(const PyStr &msg);
    PyppIOError(const std::string &msg);
};
} // namespace pypp
