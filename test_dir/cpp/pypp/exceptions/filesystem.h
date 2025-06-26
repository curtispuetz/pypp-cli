#pragma once
#include <filesystem>
#include <string>

class PyppFileNotFoundError : public std::filesystem::filesystem_error {
  public:
    PyppFileNotFoundError(const std::string &msg,
                          const std::filesystem::path &path)
        : std::filesystem::filesystem_error("PyppFileNotFoundError: " + msg,
                                            path, std::error_code()) {}
};

class PyppFileSystemError : public std::filesystem::filesystem_error {
  public:
    PyppFileSystemError(const std::string &msg,
                        const std::filesystem::path &path)
        : std::filesystem::filesystem_error("PyppFileSystemError: " + msg, path,
                                            std::error_code()) {}
};
