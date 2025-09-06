#pragma once

#include <functional>
#include <variant>

namespace pypp {

// A generic wrapper that can either own or reference a dependency
template <typename T> class PyppDependency {
    std::variant<std::reference_wrapper<T>, T> data_;

  public:
    // Construct with reference
    PyppDependency(T &ref) : data_(std::ref(ref)) {}

    // Construct by moving
    PyppDependency(T &&obj) : data_(std::move(obj)) {}

    // Accessors
    T &g() {
        if (std::holds_alternative<std::reference_wrapper<T>>(data_)) {
            return std::get<std::reference_wrapper<T>>(data_).get();
        } else {
            return std::get<T>(data_);
        }
    }
    const T &g() const {
        if (std::holds_alternative<std::reference_wrapper<T>>(data_)) {
            return std::get<std::reference_wrapper<T>>(data_).get();
        } else {
            return std::get<T>(data_);
        }
    }
};

} // namespace pypp