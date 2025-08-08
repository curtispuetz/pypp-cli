#pragma once

#include "exceptions/stdexcept.h"
#include "py_str.h"
#include "pypp_os.h"
#include "pypp_platform.h"

PyStr pypp_get_resources(const PyStr &relative_path);