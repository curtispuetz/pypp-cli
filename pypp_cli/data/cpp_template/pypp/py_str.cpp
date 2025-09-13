#include "py_str.h"
#include "exceptions/common.h"
#include <algorithm>
#include <cctype>
#include <iostream>
#include <sstream>
#include <utility>

namespace pypp {
PyStr::PyStr(std::string &&str) : s(std::move(str)) {}

PyStr PyStr::replace(const PyStr &old, const PyStr &replacement,
                     int count) const {
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
    return PyStr(std::move(result));
}

int PyStr::find(const PyStr &sub) const {
    size_t pos = s.find(sub.str());
    return (pos == std::string::npos) ? -1 : static_cast<int>(pos);
}

int PyStr::index(const PyStr &sub) const {
    int pos = find(sub);
    if (pos == -1)
        throw ValueError("substring not found");
    return pos;
}

int PyStr::rindex(const PyStr &sub) const {
    size_t pos = s.rfind(sub.str());
    if (pos == std::string::npos)
        throw ValueError("substring not found");
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
    return PyStr(std::move(result));
}

PyStr PyStr::upper() const {
    std::string result = s;
    std::transform(result.begin(), result.end(), result.begin(), ::toupper);
    return PyStr(std::move(result));
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

PyList<PyStr> PyStr::split(const PyStr &sep, int maxsplit) const {
    PyList<PyStr> result;
    size_t start = 0, end;
    while ((end = s.find(sep.str(), start)) != std::string::npos) {
        result.append(PyStr(s.substr(start, end - start)));
        start = end + sep.len();
        if (maxsplit != -1 && result.len() >= maxsplit)
            break;
    }
    result.append(PyStr(s.substr(start)));
    return result;
}

PyStr PyStr::join(const PyList<PyStr> &parts) {
    if (parts.len() == 0)
        return PyStr("");
    // Estimate total size for reserve
    size_t total = 0;
    for (size_t i = 0; i < parts.len(); ++i)
        total += parts[i].str().size();
    total += s.size() * (parts.len() - 1);

    std::string result;
    result.reserve(total);

    for (size_t i = 0; i < parts.len(); ++i) {
        result += parts[i].str();
        if (i != parts.len() - 1)
            result += s;
    }
    return PyStr(std::move(result));
}

int PyStr::len() const { return s.length(); }

PyStr PyStr::min() const {
    if (s.empty()) {
        throw ValueError("min() string argument is empty");
    }
    return PyStr(std::string(1, *std::min_element(s.begin(), s.end())));
}

PyStr PyStr::max() const {
    if (s.empty()) {
        throw ValueError("max() string argument is empty");
    }
    return PyStr(std::string(1, *std::max_element(s.begin(), s.end())));
}

std::string PyStr::repeat_string(const std::string &input, int rep) {
    if (rep <= 0)
        return "";
    std::string result;
    result.reserve(input.size() * rep);
    for (int i = 0; i < rep; ++i) {
        result += input;
    }
    return result;
}

bool PyStr::contains(const PyStr &substr) const {
    return s.find(substr.str()) != std::string::npos;
}

PyStr PyStr::operator+(const PyStr &other) const {
    return PyStr(s + other.str());
}

PyStr PyStr::operator*(const int rep) const {
    return PyStr(repeat_string(s, rep));
}

void PyStr::operator+=(const PyStr &other) { s += other.str(); }

void PyStr::operator*=(const int rep) { s = repeat_string(s, rep); }

PyStr PyStr::operator[](int i) const {
    if (i > static_cast<int>(s.length()) - 1) {
        throw IndexError("string index out of range");
    }
    if (i < 0) {
        i += s.length();
        if (i < 0)
            throw IndexError("string index out of range");
    }
    return PyStr(std::string(1, s.at(i)));
}

PyStr PyStr::operator[](const PySlice &sl) const {
    std::string result;
    PyTup<int, int, int> indices = sl.indices(static_cast<int>(s.size()));
    int start = indices.get<0>();
    int stop = indices.get<1>();
    int step = indices.get<2>();
    if (step > 0) {
        for (int i = start; i < stop; i += step) {
            result += s[i];
        }
    } else {
        for (int i = start; i > stop; i += step) {
            result += s[i];
        }
    }
    return PyStr(std::move(result));
}

const std::string &PyStr::str() const { return s; }

void PyStr::print() const { std::cout << s << std::endl; }

std::ostream &operator<<(std::ostream &os, const PyStr &pystr) {
    return os << pystr.str();
}

bool PyStr::operator==(const PyStr &other) const { return s == other.str(); }

bool PyStr::operator<(const PyStr &other) const { return s < other.str(); }

bool PyStr::operator<=(const PyStr &other) const { return s <= other.str(); }

bool PyStr::operator>(const PyStr &other) const { return s > other.str(); }

bool PyStr::operator>=(const PyStr &other) const { return s >= other.str(); }

bool PyStr::operator!=(const PyStr &other) const { return s != other.str(); }
} // namespace pypp