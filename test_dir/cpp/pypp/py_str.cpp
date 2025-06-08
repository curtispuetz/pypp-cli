#include "py_str.h"
#include <algorithm>
#include <cctype>
#include <sstream>
#include <stdexcept>
#include <iostream>

PyStr::PyStr(const std::string &str) : s(str) {}

PyStr::operator std::string() const { return s; }

void PyStr::append(const std::string &suffix) { s += suffix; }

char PyStr::pop() {
    if (s.empty())
        throw std::out_of_range("pop from empty string");
    char last = s.back();
    s.pop_back();
    return last;
}

PyStr PyStr::replace(const std::string &old, const std::string &replacement, int count) const {
    std::string result = s;
    size_t pos = 0;
    int replaced = 0;
    while ((pos = result.find(old, pos)) != std::string::npos) {
        if (count != -1 && replaced >= count)
            break;
        result.replace(pos, old.length(), replacement);
        pos += replacement.length();
        ++replaced;
    }
    return PyStr(result);
}

int PyStr::find(const std::string &sub) const {
    size_t pos = s.find(sub);
    return (pos == std::string::npos) ? -1 : static_cast<int>(pos);
}

int PyStr::index(const std::string &sub) const {
    int pos = find(sub);
    if (pos == -1)
        throw std::runtime_error("substring not found");
    return pos;
}

int PyStr::rindex(const std::string &sub) const {
    size_t pos = s.rfind(sub);
    if (pos == std::string::npos)
        throw std::runtime_error("substring not found");
    return static_cast<int>(pos);
}

int PyStr::count(const std::string &sub) const {
    int c = 0;
    size_t pos = 0;
    while ((pos = s.find(sub, pos)) != std::string::npos) {
        ++c;
        pos += sub.length();
    }
    return c;
}

bool PyStr::startswith(const std::string &prefix) const {
    return s.substr(0, prefix.size()) == prefix;
}

bool PyStr::endswith(const std::string &suffix) const {
    if (suffix.size() > s.size())
        return false;
    return s.substr(s.size() - suffix.size()) == suffix;
}

PyStr PyStr::lower() const {
    std::string result = s;
    std::transform(result.begin(), result.end(), result.begin(), ::tolower);
    return PyStr(result);
}

PyStr PyStr::upper() const {
    std::string result = s;
    std::transform(result.begin(), result.end(), result.begin(), ::toupper);
    return PyStr(result);
}

PyStr PyStr::strip() const {
    size_t start = s.find_first_not_of(" \t\n\r\f\v");
    size_t end = s.find_last_not_of(" \t\n\r\f\v");
    return (start == std::string::npos)
               ? PyStr("")
               : PyStr(s.substr(start, end - start + 1));
}

PyStr PyStr::lstrip() const {
    size_t start = s.find_first_not_of(" \t\n\r\f\v");
    return (start == std::string::npos) ? PyStr("") : PyStr(s.substr(start));
}

PyStr PyStr::rstrip() const {
    size_t end = s.find_last_not_of(" \t\n\r\f\v");
    return (end == std::string::npos) ? PyStr("") : PyStr(s.substr(0, end + 1));
}

std::vector<PyStr> PyStr::split(const std::string &sep) const {
    std::vector<PyStr> result;
    size_t start = 0, end;
    while ((end = s.find(sep, start)) != std::string::npos) {
        result.emplace_back(s.substr(start, end - start));
        start = end + sep.length();
    }
    result.emplace_back(s.substr(start));
    return result;
}

PyStr PyStr::join(const std::string &sep, const std::vector<PyStr> &parts) {
    std::ostringstream oss;
    for (size_t i = 0; i < parts.size(); ++i) {
        oss << static_cast<std::string>(parts[i]);
        if (i != parts.size() - 1)
            oss << sep;
    }
    return PyStr(oss.str());
}

size_t PyStr::len() const {
    return s.length();
}

PyStr PyStr::operator+(const PyStr &other) const {
    return PyStr(s + other.str());
}

PyStr PyStr::operator[](int i) const {
    if (i < 0) {
        i += s.length();
        if (i < 0)
            throw std::out_of_range("index out of range");
    }
    return PyStr(std::string(1, s.at(i)));
}

PyStr PyStr::slice(int start, int stop, int step) const {
    std::string result;
    int n = static_cast<int>(s.size());

    // Handle negative indexing
    if (start < 0) start += n;
    if (stop < 0) stop += n;

    // Clamp boundaries
    if (start < 0) start = 0;
    if (stop > n) stop = n;

    if (step > 0 && start < stop) {
        for (int i = start; i < stop; i += step)
            result += s[i];
    } else if (step < 0 && start > stop) {
        for (int i = start; i > stop; i += step)
            result += s[i];
    }

    return PyStr(result);
}

PyStr PyStr::operator[](const PySlice &sl) const {
    return slice(sl.start, sl.stop, sl.step);
}

std::string PyStr::str() const {
    return s;
}

void PyStr::print() const {
    std::cout << s << std::endl;
}

bool PyStr::operator==(const PyStr &other) const {
    return s == other.str();
}

bool PyStr::operator<(const PyStr &other) const {
    return s < other.str();
}

bool PyStr::operator<=(const PyStr &other) const {
    return s <= other.str();
}

bool PyStr::operator>(const PyStr &other) const {
    return s > other.str();
}

bool PyStr::operator>=(const PyStr &other) const {
    return s >= other.str();
}

bool PyStr::operator!=(const PyStr &other) const {
    return s != other.str();
}
