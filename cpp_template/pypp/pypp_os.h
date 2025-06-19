#pragma once

#include "py_list.h"
#include "py_str.h"
#include "py_tuple.h"
#include <filesystem>
#include <numeric>
#include <vector>

namespace os {

namespace fs = std::filesystem;

/**
 * @brief Recursively creates directories.
 */
inline bool makedirs(const PyStr &p) {
    return fs::create_directories(fs::path(p.str()));
}

/**
 * @brief Removes a file.
 */
inline bool remove(const PyStr &p) { return fs::remove(fs::path(p.str())); }

/**
 * @brief Creates a single directory.
 */
inline bool mkdir(const PyStr &p) {
    return fs::create_directory(fs::path(p.str()));
}

/**
 * @brief Removes an empty directory.
 */
inline bool rmdir(const PyStr &p) {
    // fs::remove is used for both files and empty directories
    return fs::remove(fs::path(p.str()));
}

/**
 * @brief Recursively removes directories. All subdirectories and files will
 * also be removed.
 */
inline void removedirs(const PyStr &p) { fs::remove_all(fs::path(p.str())); }

/**
 * @brief Renames a file or directory.
 */
inline void rename(const PyStr &old_p, const PyStr &new_p) {
    fs::rename(fs::path(old_p.str()), fs::path(new_p.str()));
}

/**
 * @brief Lists the contents of a directory.
 */
inline PyList<PyStr> listdir(const PyStr &p) {
    PyList<PyStr> entries;
    for (const auto &entry : fs::directory_iterator(fs::path(p.str()))) {
        entries.append(PyStr(entry.path().filename().string()));
    }
    return entries;
}

namespace path {

/**
 * @brief Joins one or more path components intelligently.
 */
template <typename... Args> PyStr join(const PyStr &base, const Args &...args) {
    fs::path result(base.str());
    // This fold expression efficiently joins all arguments
    (result /= ... /= fs::path(args.str()));
    return result.string();
}

/**
 * @brief Checks if a path exists.
 */
inline bool exists(const PyStr &p) { return fs::exists(fs::path(p.str())); }

/**
 * @brief Checks if a path is a directory.
 */
inline bool isdir(const PyStr &p) {
    return fs::is_directory(fs::path(p.str()));
}

/**
 * @brief Checks if a path is a file.
 */
inline bool isfile(const PyStr &p) {
    return fs::is_regular_file(fs::path(p.str()));
}

/**
 * @brief Returns the directory name of a path.
 */
inline PyStr dirname(const PyStr &p) {
    return PyStr(fs::path(p.str()).parent_path().string());
}

/**
 * @brief Returns the base name of a path.
 */
inline PyStr basename(const PyStr &p) {
    return PyStr(fs::path(p.str()).filename().string());
}

/**
 * @brief Splits a path into a (head, tail) pair.
 */
inline PyTup<PyStr, PyStr> split(const PyStr &p) {
    fs::path path_obj(p.str());
    return PyTup(PyStr(path_obj.parent_path().string()),
                 PyStr(path_obj.filename().string()));
}

/**
 * @brief Returns the absolute version of a path.
 */
inline PyStr abspath(const PyStr &p) {
    return PyStr(fs::absolute(fs::path(p.str())).string());
}

} // namespace path
} // namespace os