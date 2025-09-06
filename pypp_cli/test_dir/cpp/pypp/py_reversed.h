#pragma once

#include <iterator> // For std::rbegin, std::rend, std::crbegin, std::crend
#include <utility>  // For std::forward

namespace pypp {
// The main PyReversed class (the "range")
template <typename T> class PyReversed {
  public:
    // Constructor uses a universal reference to handle both lvalues and rvalues
    PyReversed(T &&iterable) : _iterable(std::forward<T>(iterable)) {}

    // For non-const range-based for loops. Returns a mutable reverse_iterator.
    auto begin() { return std::rbegin(_iterable); }

    auto end() { return std::rend(_iterable); }

    // For const range-based for loops. Returns a const_reverse_iterator.
    // This overload is chosen when the PyReversed object itself is const.
    auto begin() const { return std::crbegin(_iterable); }

    auto end() const { return std::crend(_iterable); }

  private:
    T _iterable;
};

// C++17 Deduction Guide for easier instantiation (e.g., PyReversed(my_vec))
template <typename T> PyReversed(T &&) -> PyReversed<T>;
} // namespace pypp