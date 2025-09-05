#pragma once

#include "exceptions/exception.h"
#include "py_str.h"

class CustomException : public PyppException {
  public:
    explicit CustomException(const PyStr &msg)
        : PyppException(PyStr("CustomException: ") + msg) {}
};

class ChildException : public CustomException {
  public:
    explicit ChildException(const PyStr &msg)
        : CustomException(PyStr("ChildException: ") + msg) {}
};

void custom_exception_fn();