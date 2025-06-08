#pragma once

#include <string>
#include <vector>
#include "py_slice.h"

class PyStr {
    std::string s;
    PyStr slice(int start, int stop, int step = 1) const;

public:
    PyStr(const std::string &str = "");

    operator std::string() const;

    void append(const std::string &suffix);
    char pop();
    PyStr replace(const std::string &old, const std::string &replacement, int count = -1) const;
    int find(const std::string &sub) const;
    int index(const std::string &sub) const;
    int rindex(const std::string &sub) const;
    int count(const std::string &sub) const;
    bool startswith(const std::string &prefix) const;
    bool endswith(const std::string &suffix) const;
    PyStr lower() const;
    PyStr upper() const;
    PyStr strip() const;
    PyStr lstrip() const;
    PyStr rstrip() const;
    std::vector<PyStr> split(const std::string &sep = " ") const;
    static PyStr join(const std::string &sep, const std::vector<PyStr> &parts);
    size_t len() const;

    PyStr operator+(const PyStr &other) const;
    PyStr operator[](int i) const;
    PyStr operator[](const PySlice &sl) const;

    bool operator==(const PyStr &other) const;
    bool operator<(const PyStr &other) const;
    bool operator<=(const PyStr &other) const;
    bool operator>(const PyStr &other) const;
    bool operator>=(const PyStr &other) const;
    bool operator!=(const PyStr &other) const;

    std::string str() const;
    void print() const;
};