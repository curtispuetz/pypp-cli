#include "py_str.h"
#include <algorithm>
#include <cctype>
#include <sstream>
#include <stdexcept>
#include <iostream>

PyStr::PyStr(const std::string &str) : s(str) {}

PyStr PyStr::replace(const PyStr &old, const PyStr &replacement, int count) const {
    std::string result = s;
    size_t pos = 0;
    int replaced = 0;
    while ((pos = result.find(old.str(), pos)) != std::string::npos) {
        if (count != -1 && replaced >= count)
            break;
        result.replace(pos, old.len(), replacement.str());
        pos += replacement.len();
        ++replaced;
    }
    return PyStr(result);
}

int PyStr::find(const PyStr &sub) const {
    size_t pos = s.find(sub.str());
    return (pos == std::string::npos) ? -1 : static_cast<int>(pos);
}

int PyStr::index(const PyStr &sub) const {
    int pos = find(sub);
    if (pos == -1)
        throw std::runtime_error("substring not found");
    return pos;
}

int PyStr::rindex(const PyStr &sub) const {
    size_t pos = s.rfind(sub.str());
    if (pos == std::string::npos)
        throw std::runtime_error("substring not found");
    return static_cast<int>(pos);
}

int PyStr::count(const PyStr &sub) const {
    int c = 0;
    size_t pos = 0;
    while ((pos = s.find(sub.str(), pos)) != std::string::npos) {
        ++c;
        pos += sub.len();
    }
    return c;
}

bool PyStr::startswith(const PyStr &prefix) const {
    return s.substr(0, prefix.len()) == prefix.str();
}

bool PyStr::endswith(const PyStr &suffix) const {
    if (suffix.len() > s.size())
        return false;
    return s.substr(s.size() - suffix.len()) == suffix.str();
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

std::vector<PyStr> PyStr::split(const PyStr &sep) const {
    std::vector<PyStr> result;
    size_t start = 0, end;
    while ((end = s.find(sep.str(), start)) != std::string::npos) {
        result.emplace_back(s.substr(start, end - start));
        start = end + sep.len();
    }
    result.emplace_back(s.substr(start));
    return result;
}

PyStr PyStr::join(const std::vector<PyStr> &parts) {
    std::ostringstream oss;
    for (size_t i = 0; i < parts.size(); ++i) {
        oss << parts[i].str();
        if (i != parts.size() - 1)
            oss << s;
    }
    return PyStr(oss.str());
}

size_t PyStr::len() const {
    return s.length();
}

std::string PyStr::repeat_string(const std::string& input, int rep) {
        if (rep <= 0) return "";
        std::string result;
        result.reserve(input.size() * rep);
        for (int i = 0; i < rep; ++i) {
            result += input;
        }
        return result;
    }

PyStr PyStr::operator+(const PyStr &other) const {
    return PyStr(s + other.str());
}

PyStr PyStr::operator*(const int rep) const {
    return PyStr(repeat_string(s, rep));
}

void PyStr::operator+=(const PyStr& other) {
    s += other.str();
}

void PyStr::operator*=(const int rep) {
    s = repeat_string(s, rep);
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
