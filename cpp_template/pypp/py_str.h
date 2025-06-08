#pragma once

#include <string>
#include <vector>

class PyString {
    std::string s;

public:
    PyString(const std::string &str = "");

    operator std::string() const;

    void append(const std::string &suffix);
    char pop();
    PyString replace(const std::string &old, const std::string &replacement, int count = -1) const;
    int find(const std::string &sub) const;
    int index(const std::string &sub) const;
    int rindex(const std::string &sub) const;
    int count(const std::string &sub) const;
    bool startswith(const std::string &prefix) const;
    bool endswith(const std::string &suffix) const;
    PyString lower() const;
    PyString upper() const;
    PyString strip() const;
    PyString lstrip() const;
    PyString rstrip() const;
    std::vector<PyString> split(const std::string &sep = " ") const;
    static PyString join(const std::string &sep, const std::vector<PyString> &parts);
    size_t length() const;

    char operator[](int i) const;
    std::string str() const;
};