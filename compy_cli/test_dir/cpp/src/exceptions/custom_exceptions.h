#pragma once

#include "exceptions/exception.h"

class CustomException : public PyppException {
  public:
    explicit CustomException(const std::string &msg)
        : PyppException("CustomException: " + msg) {}
};

class ChildException : public CustomException {
  public:
    explicit ChildException(const std::string &msg)
        : CustomException("ChildException: " + msg) {}
};

void custom_exception_fn();