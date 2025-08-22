#include "compy_resources.h"

PyStr compy_get_resources(const PyStr &relative_path) {
    PyStr exe_dir = platform::get_executable_dir();
    return os::path::join(exe_dir, PyStr(".."), PyStr(".."), PyStr(".."),
                          PyStr("resources"), relative_path);
}