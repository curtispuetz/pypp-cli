#include "exceptions/filesystem.h"
#include "py_str.h"

namespace pypp {

OSError::OSError(const PyStr &msg) : Exception(PyStr("OSError: ") + msg) {}

FileNotFoundError::FileNotFoundError(const PyStr &msg)
    : OSError(PyStr("FileNotFoundError: ") + msg) {}

NotADirectoryError::NotADirectoryError(const PyStr &msg)
    : OSError(PyStr("NotADirectoryError: ") + msg) {}

PermissionError::PermissionError(const PyStr &msg)
    : OSError(PyStr("PermissionError: ") + msg) {}

FileExistsError::FileExistsError(const PyStr &msg)
    : OSError(PyStr("FileExistsError: ") + msg) {}

} // namespace pypp