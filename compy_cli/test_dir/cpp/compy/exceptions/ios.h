#pragma once
#include <ios>
#include <string>

class CompyIOError : public std::ios_base::failure {
  public:
    explicit CompyIOError(const std::string &msg)
        : std::ios_base::failure("CompyIOError: " + msg) {}
};
