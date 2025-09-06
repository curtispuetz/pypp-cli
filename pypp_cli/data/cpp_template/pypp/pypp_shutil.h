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
    std::filesystem::remove_all(fs_path, ec);
    if (ec) {
        throw PyppFileSystemError("shutil::rmtree failed", fs_path);
    }
}
} // namespace shutil
} // namespace pypp