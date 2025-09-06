#pragma once

#include "py_list.h"
#include "slice/py_slice.h"
#include <format>
#include <optional>
#include <ostream>
#include <sstream>
#include <string>

namespace pypp {
class PyStr {
    std::string s;
    static std::string repeat_string(const std::string &input, int rep);

    class iterator {
      public:
        // C++20 Iterator Traits
        using iterator_concept = std::forward_iterator_tag;
        using iterator_category = std::forward_iterator_tag;
        using value_type = PyStr;
        using difference_type = std::ptrdiff_t;
        using pointer = PyStr *;
        using reference =
            PyStr; // Returning by value, so reference is the value type

        iterator(std::string::const_iterator it) : m_it(it) {}

        // Dereference operator: Returns a PyStr of the current character
        reference operator*() const { return PyStr(std::string(1, *m_it)); }

        // Pre-increment operator
        iterator &operator++() {
            m_it++;
            return *this;
        }

        // Post-increment operator
        iterator operator++(int) {
            iterator tmp = *this;
            ++(*this);
            return tmp;
        }

        // Equality operators
        friend bool operator==(const iterator &a, const iterator &b) {
            return a.m_it == b.m_it;
        };

        friend bool operator!=(const iterator &a, const iterator &b) {
            return a.m_it != b.m_it;
        };

      private:
        std::string::const_iterator m_it;
    };

    class reverse_iterator {
      public:
        // C++ Iterator Traits
        using iterator_category = std::forward_iterator_tag;
        using value_type = PyStr;
        using difference_type = std::ptrdiff_t;
        using pointer = PyStr *;
        using reference = PyStr; // Returning by value

        // Constructor takes the underlying string's reverse iterator
        reverse_iterator(std::string::const_reverse_iterator it) : m_it(it) {}

        // Dereference operator: Returns a PyStr of the current character
        reference operator*() const { return PyStr(std::string(1, *m_it)); }

        // Pre-increment operator
        reverse_iterator &operator++() {
            m_it++;
            return *this;
        }

        // Post-increment operator
        reverse_iterator operator++(int) {
            reverse_iterator tmp = *this;
            ++(*this);
            return tmp;
        }

        // Equality operators
        friend bool operator==(const reverse_iterator &a,
                               const reverse_iterator &b) {
            return a.m_it == b.m_it;
        };
        friend bool operator!=(const reverse_iterator &a,
                               const reverse_iterator &b) {
            return a.m_it != b.m_it;
        };

      private:
        std::string::const_reverse_iterator m_it;
    };

  public:
    inline iterator begin() { return iterator(s.cbegin()); }
    inline iterator end() { return iterator(s.cend()); }
    inline iterator begin() const { return iterator(s.cbegin()); }
    inline iterator end() const { return iterator(s.cend()); }
    // Reverse iterator support
    inline reverse_iterator rbegin() { return reverse_iterator(s.crbegin()); }
    inline reverse_iterator rend() { return reverse_iterator(s.crend()); }

    inline reverse_iterator rbegin() const {
        return reverse_iterator(s.crbegin());
    }
    inline reverse_iterator rend() const { return reverse_iterator(s.crend()); }

    PyStr(std::string &&str = "");

    PyStr replace(const PyStr &old, const PyStr &replacement,
                  int count = -1) const;
    int find(const PyStr &sub) const;
    int index(const PyStr &sub) const;
    int rindex(const PyStr &sub) const;
    int count(const PyStr &sub) const;
    bool startswith(const PyStr &prefix) const;
    bool endswith(const PyStr &suffix) const;
    PyStr lower() const;
    PyStr upper() const;
    PyStr strip() const;
    PyStr lstrip() const;
    PyStr rstrip() const;
    PyList<PyStr> split(const PyStr &sep = PyStr(" ")) const;
    PyStr join(const PyList<PyStr> &parts);
    int len() const;
    bool contains(const PyStr &substr) const;

    PyStr operator+(const PyStr &other) const;
    PyStr operator*(const int rep) const;
    void operator+=(const PyStr &other);
    void operator*=(const int rep);
    PyStr operator[](int i) const;
    PyStr operator[](const PySlice &sl) const;

    bool operator==(const PyStr &other) const;
    bool operator<(const PyStr &other) const;
    bool operator<=(const PyStr &other) const;
    bool operator>(const PyStr &other) const;
    bool operator>=(const PyStr &other) const;
    bool operator!=(const PyStr &other) const;

    const std::string &str() const;
    void print() const;
    friend std::ostream &operator<<(std::ostream &os, const PyStr &pystr);
};

} // namespace pypp

namespace std {
// Hash function for usage as a key in PyDict and PySet
template <> struct hash<pypp::PyStr> {
    std::size_t operator()(const pypp::PyStr &p) const noexcept {
        return std::hash<std::string>()(p.str());
    }
};

// Formatter for std::format
template <> struct formatter<pypp::PyStr, char> {
    constexpr auto parse(format_parse_context &ctx) { return ctx.begin(); }

    template <typename FormatContext>
    auto format(const pypp::PyStr &p, FormatContext &ctx) const {
        return std::format_to(ctx.out(), "{}", p.str());
    }
};
} // namespace std