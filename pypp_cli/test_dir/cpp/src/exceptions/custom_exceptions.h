#pragma once

#include "exceptions/exception.h"
#include "py_str.h"

class CustomException : public pypp::PyppException {
  public:
    explicit CustomException(const pypp::PyStr &msg)
        : pypp::PyppException(pypp::PyStr("CustomException: ") + msg) {}
};

class ChildException : public CustomException {
  public:
    explicit ChildException(const pypp::PyStr &msg)
        : CustomException(pypp::PyStr("ChildException: ") + msg) {}
};

void custom_exception_fn();