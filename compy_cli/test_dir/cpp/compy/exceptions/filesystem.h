#pragma once
#include <filesystem>
#include <string>

class CompyFileNotFoundError : public std::filesystem::filesystem_error {
  public:
    CompyFileNotFoundError(const std::string &msg,
                           const std::filesystem::path &path)
        : std::filesystem::filesystem_error("CompyFileNotFoundError: " + msg,
                                            path, std::error_code()) {}
};

class CompyFileSystemError : public std::filesystem::filesystem_error {
  public:
    CompyFileSystemError(const std::string &msg,
                         const std::filesystem::path &path)
        : std::filesystem::filesystem_error("CompyFileSystemError: " + msg,
                                            path, std::error_code()) {}
};
