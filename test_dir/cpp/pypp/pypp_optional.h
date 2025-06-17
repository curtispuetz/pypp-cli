#pragma once
#include "exceptions/stdexcept.h"
#include <iostream>
#include <optional>

template <typename T> class PyppOpt {
  private:
    std::optional<std::reference_wrapper<T>> _value;

  public:
    PyppOpt() = default;

    PyppOpt(T &ref) : _value(ref) {}

    bool has_value() const { return _value.has_value(); }

    T &value() {
        if (!_value) {
            throw PyppValueError("Optional has no value");
        }
        return _value.value().get();
    }

    T value_or(const T &default_value) const {
        return _value ? _value.value().get() : default_value;
    }

    void reset() { _value.reset(); }

    void emplace(T &ref) { _value = ref; }

    explicit operator bool() const { return has_value(); }
};