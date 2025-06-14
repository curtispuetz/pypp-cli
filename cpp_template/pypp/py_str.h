#pragma once

#include "py_list.h"
#include "py_slice.h"
#include <optional>
#include <ostream>
#include <string>

class PyStr {
    std::string s;
    PyStr slice(int start, std::optional<int> stop, int step = 1) const;
    static std::string repeat_string(const std::string &input, int rep);

  public:
    PyStr(const std::string &str = "");

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

namespace std {
template <> struct hash<PyStr> {
    std::size_t operator()(const PyStr &p) const noexcept {
        return std::hash<std::string>()(p.str());
    }
};
} // namespace std
