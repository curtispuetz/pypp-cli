#pragma once

#include "compy_os.h"
#include "compy_platform.h"
#include "exceptions/stdexcept.h"
#include "py_str.h"

PyStr compy_get_resources(const PyStr &relative_path);