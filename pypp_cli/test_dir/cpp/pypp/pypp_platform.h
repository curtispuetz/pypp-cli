#pragma once

#include <py_str.h>

namespace pypp {
namespace platform {

/**
 * @brief Gets the directory where the current executable is located.
 */
PyStr get_executable_dir(); // Declaration only

} // namespace platform
} // namespace pypp