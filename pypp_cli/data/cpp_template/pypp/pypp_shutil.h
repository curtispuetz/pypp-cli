#pragma once
#include "exceptions/filesystem.h"
#include "py_str.h"
#include <filesystem>
#include <string>

namespace pypp {
namespace shutil {
// Recursively deletes a directory and all its contents, like Python's
// shutil.rmtree(path)
inline void rmtree(const PyStr &path) {
    std::error_code ec;
    std::filesystem::path fs_path(path.str());
    if (!std::filesystem::exists(fs_path)) {
        throw FileNotFoundError(
            PyStr("The system cannot find the file specified: ") + path);
    }
    if (!std::filesystem::is_directory(fs_path)) {
        throw NotADirectoryError(PyStr("The directory name is invalid: ") +
                                 path);
    }
    std::filesystem::remove_all(fs_path, ec);
    if (ec) {
        if (ec == std::errc::permission_denied) {
            throw PermissionError(PyStr("Permission denied: ") + path);
        }
        throw OSError(PyStr("[Error code: ") + std::to_string(ec.value()) +
                      PyStr("] shutil::rmtree failed: ") + path);
    }
}
} // namespace shutil
} // namespace pypp