#pragma once

#include "exceptions/stdexcept.h"
#include "pypp_util/print_py_value.h"
#include <any>
#include <format>
#include <iostream>
#include <tuple>
#include <utility>

template <typename... Args> class PyTup {
  private:
    std::tuple<Args...> data;

    // Count helper
    template <typename T, std::size_t I = 0>
    static constexpr std::size_t count_impl(const std::tuple<Args...> &tup,
                                            const T &value) {
        if constexpr (I == sizeof...(Args)) {
            return 0; // Base case: end of the tuple
        } else {
            size_t current_count = 0;
            // First, check if the types are the same before comparing values
            if constexpr (std::is_same_v<
                              std::tuple_element_t<I, std::tuple<Args...>>,
                              T>) {
                if (std::get<I>(tup) == value) {
                    current_count = 1;
                }
            }
            // Continue recursively with the rest of the tuple
            return current_count + count_impl<T, I + 1>(tup, value);
        }
    }

    // Index helper
    template <typename T, std::size_t I = 0>
    static constexpr std::size_t index_impl(const std::tuple<Args...> &tup,
                                            const T &value) {
        if constexpr (I == sizeof...(Args)) {
            throw PyppValueError("tuple.index(x): x not in tuple");
        } else {
            // Check if types are compatible before comparison
            if constexpr (std::is_same_v<
                              std::tuple_element_t<I, std::tuple<Args...>>,
                              T>) {
                if (std::get<I>(tup) == value) {
                    return I;
                }
            }
            // Otherwise, just continue the search
            return index_impl<T, I + 1>(tup, value);
        }
    }

    // Helper for printing (now takes an ostream reference)
    template <std::size_t I = 0> void print_impl(std::ostream &os) const {
        if constexpr (I < sizeof...(Args)) {
            print_py_value(os, std::get<I>(data));
            if constexpr (I + 1 < sizeof...(Args)) {
                os << ", ";
            }
            print_impl<I + 1>(
                os); // Pass the ostream to the next recursive call
        }
    }

  public:
    // Rvalue-only constructor for value types
    PyTup(Args &&...args) : data(std::move(args)...) {}
    // Allow construction from lvalues if all Args are references (for PyDict
    // iterator, etc.)
    template <
        typename Dummy = void,
        std::enable_if_t<(std::is_reference_v<Args> && ...), Dummy> * = nullptr>
    PyTup(Args... args) : data(args...) {}

    // Count method
    template <typename T> int count(const T &value) const {
        return count_impl<T>(data, value);
    }

    // Index method
    template <typename T> int index(const T &value) const {
        return index_impl<T>(data, value);
    }

    // Compile-time access: Idiomatic, efficient, and fully typed
    template <std::size_t I> auto &get() {
        // NOTE: I think this is actually unnessary because if it is true it
        // results in a compile-time error anyway.
        if (I >= sizeof...(Args)) {
            throw PyppIndexError("tuple index out of range");
        }
        return std::get<I>(data);
    }

    // TODO later: delete this because I think I don't need it.
    template <std::size_t I> const auto &get() const {
        if (I >= sizeof...(Args)) {
            throw PyppIndexError("tuple index out of range");
        }
        return std::get<I>(data);
    }

    // Length method
    int len() const { return sizeof...(Args); }

    // Print method (now calls print_impl with std::cout)
    void print() const {
        print(std::cout); // Default to printing to std::cout
        std::cout << std::endl;
    }

    // Overloaded print method to print to any ostream
    void print(std::ostream &os) const {
        os << "(";
        print_impl(os); // Pass the ostream to the helper
        os << ")";
    }

    // Comparison operators
    bool operator==(const PyTup &other) const { return data == other.data; }
    bool operator!=(const PyTup &other) const { return data != other.data; }
    bool operator<(const PyTup &other) const { return data < other.data; }
    bool operator<=(const PyTup &other) const { return data <= other.data; }
    bool operator>(const PyTup &other) const { return data > other.data; }
    bool operator>=(const PyTup &other) const { return data >= other.data; }

    // raw access to the underlying tuple
    const std::tuple<Args...> &raw() const { return data; }

    // Friend declaration for the stream insertion operator
    // This allows the operator to access private members if needed (though
    // print() is public)
    template <typename... OtherArgs>
    friend std::ostream &operator<<(std::ostream &os,
                                    const PyTup<OtherArgs...> &tup);
};

// dedction guide
template <typename... Ts> PyTup(Ts...) -> PyTup<Ts...>;

// Stream insertion operator overload
template <typename... Args>
std::ostream &operator<<(std::ostream &os, const PyTup<Args...> &tup) {
    tup.print(os); // Call the flexible print method
    return os;     // Return the ostream reference to allow chaining
}

namespace std {
// Hash function for usage as a key in PyDict and PySet
template <typename... Args> struct hash<PyTup<Args...>> {
    std::size_t operator()(const PyTup<Args...> &tup) const noexcept {
        return std::apply(
            [](const auto &...args) {
                return (std::hash<std::decay_t<decltype(args)>>{}(args) ^ ...);
            },
            tup.raw());
    }
};

// Formatter for std::format
template <typename... Args> struct formatter<PyTup<Args...>, char> {
    constexpr auto parse(format_parse_context &ctx) { return ctx.begin(); }

    template <typename FormatContext>
    auto format(const PyTup<Args...> &tup, FormatContext &ctx) const {
        std::ostringstream oss;
        tup.print(oss); // Use the print method to format the tuple
        return std::format_to(ctx.out(), "{}", oss.str());
    }
};

// Structured bindings support for PyTup
template <typename... Args>
struct tuple_size<PyTup<Args...>>
    : std::integral_constant<std::size_t, sizeof...(Args)> {};

template <std::size_t I, typename... Args>
struct tuple_element<I, PyTup<Args...>> {
    using type = std::tuple_element_t<I, std::tuple<Args...>>;
};
} // namespace std