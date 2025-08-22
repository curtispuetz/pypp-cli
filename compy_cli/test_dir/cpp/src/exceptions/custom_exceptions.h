#pragma once

#include "exceptions/exception.h"

class CustomException : public CompyException {
  public:
    explicit CustomException(const std::string &msg)
        : CompyException("CustomException: " + msg) {}
};

class ChildException : public CustomException {
  public:
    explicit ChildException(const std::string &msg)
        : CustomException("ChildException: " + msg) {}
};

void custom_exception_fn();