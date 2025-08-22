#pragma once
#include <ios>
#include <string>

class PyppIOError : public std::ios_base::failure {
  public:
    explicit PyppIOError(const std::string &msg)
        : std::ios_base::failure("PyppIOError: " + msg) {}
};
