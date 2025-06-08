#include "py_str.h"
#include <algorithm>
#include <cctype>
#include <sstream>
#include <stdexcept>

PyString::PyString(const std::string &str) : s(str) {}

PyString::operator std::string() const { return s; }

void PyString::append(const std::string &suffix) { s += suffix; }

char PyString::pop() {
    if (s.empty())
        throw std::out_of_range("pop from empty string");
    char last = s.back();
    s.pop_back();
    return last;
}

PyString PyString::replace(const std::string &old, const std::string &replacement, int count) const {
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
    return PyString(result);
}

int PyString::find(const std::string &sub) const {
    size_t pos = s.find(sub);
    return (pos == std::string::npos) ? -1 : static_cast<int>(pos);
}

int PyString::index(const std::string &sub) const {
    int pos = find(sub);
    if (pos == -1)
        throw std::runtime_error("substring not found");
    return pos;
}

int PyString::rindex(const std::string &sub) const {
    size_t pos = s.rfind(sub);
    if (pos == std::string::npos)
        throw std::runtime_error("substring not found");
    return static_cast<int>(pos);
}

int PyString::count(const std::string &sub) const {
    int c = 0;
    size_t pos = 0;
    while ((pos = s.find(sub, pos)) != std::string::npos) {
        ++c;
        pos += sub.length();
    }
    return c;
}

bool PyString::startswith(const std::string &prefix) const {
    return s.substr(0, prefix.size()) == prefix;
}

bool PyString::endswith(const std::string &suffix) const {
    if (suffix.size() > s.size())
        return false;
    return s.substr(s.size() - suffix.size()) == suffix;
}

PyString PyString::lower() const {
    std::string result = s;
    std::transform(result.begin(), result.end(), result.begin(), ::tolower);
    return PyString(result);
}

PyString PyString::upper() const {
    std::string result = s;
    std::transform(result.begin(), result.end(), result.begin(), ::toupper);
    return PyString(result);
}

PyString PyString::strip() const {
    size_t start = s.find_first_not_of(" \t\n\r\f\v");
    size_t end = s.find_last_not_of(" \t\n\r\f\v");
    return (start == std::string::npos)
               ? PyString("")
               : PyString(s.substr(start, end - start + 1));
}

PyString PyString::lstrip() const {
    size_t start = s.find_first_not_of(" \t\n\r\f\v");
    return (start == std::string::npos) ? PyString("") : PyString(s.substr(start));
}

PyString PyString::rstrip() const {
    size_t end = s.find_last_not_of(" \t\n\r\f\v");
    return (end == std::string::npos) ? PyString("") : PyString(s.substr(0, end + 1));
}

std::vector<PyString> PyString::split(const std::string &sep) const {
    std::vector<PyString> result;
    size_t start = 0, end;
    while ((end = s.find(sep, start)) != std::string::npos) {
        result.emplace_back(s.substr(start, end - start));
        start = end + sep.length();
    }
    result.emplace_back(s.substr(start));
    return result;
}

PyString PyString::join(const std::string &sep, const std::vector<PyString> &parts) {
    std::ostringstream oss;
    for (size_t i = 0; i < parts.size(); ++i) {
        oss << static_cast<std::string>(parts[i]);
        if (i != parts.size() - 1)
            oss << sep;
    }
    return PyString(oss.str());
}

size_t PyString::length() const {
    return s.length();
}

char PyString::operator[](int i) const {
    if (i < 0) {
        i += s.length();
        if (i < 0)
            throw std::out_of_range("index out of range");
    }
    return s.at(i);
}

std::string PyString::str() const {
    return s;
}