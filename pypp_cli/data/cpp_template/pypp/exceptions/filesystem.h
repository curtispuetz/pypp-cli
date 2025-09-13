#pragma once
#include <filesystem>
#include <string>

namespace pypp {
class FileNotFoundError : public std::filesystem::filesystem_error {
  public:
    FileNotFoundError(const std::string &msg, const std::filesystem::path &path)
        : std::filesystem::filesystem_error("FileNotFoundError: " + msg, path,
                                            std::error_code()) {}
};

class FileSystemError : public std::filesystem::filesystem_error {
  public:
    FileSystemError(const std::string &msg, const std::filesystem::path &path)
        : std::filesystem::filesystem_error("FileSystemError: " + msg, path,
                                            std::error_code()) {}
};

} // namespace pypp
