#pragma once

#include "exceptions/exception.h"
#include "exceptions/stdexcept.h"
#include "py_str.h"

namespace me {
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

class CustomValueError : public pypp::PyppValueError {
  public:
    explicit CustomValueError(const pypp::PyStr &msg)
        : pypp::PyppValueError(pypp::PyStr("CustomValueError: ") + msg) {}
};

void custom_exception_fn();
} // namespace me