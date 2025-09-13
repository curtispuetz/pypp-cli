#pragma once

#include "exceptions/exception.h"

namespace pypp {
class PyStr;

class OSError : public Exception {
  public:
    OSError(const PyStr &msg);
};

class FileNotFoundError : public OSError {
  public:
    FileNotFoundError(const PyStr &msg);
};

class FileSystemError : public OSError {
  public:
    FileSystemError(const PyStr &msg);
};

class NotADirectoryError : public OSError {
  public:
    NotADirectoryError(const PyStr &msg);
};

class PermissionError : public OSError {
  public:
    PermissionError(const PyStr &msg);
};

class FileExistsError : public OSError {
  public:
    FileExistsError(const PyStr &msg);
};

} // namespace pypp
