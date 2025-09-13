#pragma once

#include "exceptions/exception.h"
#include "exceptions/stdexcept.h"
#include "py_str.h"

namespace me {
class CustomException : public pypp::Exception {
  public:
    explicit CustomException(const pypp::PyStr &msg)
        : pypp::Exception(pypp::PyStr("CustomException: ") + msg) {}
};

class ChildException : public CustomException {
  public:
    explicit ChildException(const pypp::PyStr &msg)
        : CustomException(pypp::PyStr("ChildException: ") + msg) {}
};

class CustomValueError : public pypp::ValueError {
  public:
    explicit CustomValueError(const pypp::PyStr &msg)
        : pypp::ValueError(pypp::PyStr("CustomValueError: ") + msg) {}
};

void custom_exception_fn();
} // namespace me