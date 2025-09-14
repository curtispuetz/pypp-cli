#pragma once

#include "py_list.h"
#include "py_str.h"
#include "py_tuple.h"
#include <filesystem>
#include <numeric>
#include <vector>

namespace pypp {
namespace os {

namespace fs = std::filesystem;

void makedirs(const PyStr &p);
void mkdir(const PyStr &p);
void remove(const PyStr &p);
void rmdir(const PyStr &p);
void rename(const PyStr &src, const PyStr &dst);

PyList<PyStr> listdir(const PyStr &p);

namespace path {

template <typename... Args> PyStr join(const PyStr &base, const Args &...args) {
    fs::path result(base.str());
    // This fold expression efficiently joins all arguments
    (result /= ... /= fs::path(args.str()));
    return result.string();
}

bool exists(const PyStr &p);
bool isdir(const PyStr &p);
bool isfile(const PyStr &p);
PyStr dirname(const PyStr &p);
PyStr basename(const PyStr &p);
PyTup<PyStr, PyStr> split(const PyStr &p);
PyStr abspath(const PyStr &p);

} // namespace path
} // namespace os
} // namespace pypp