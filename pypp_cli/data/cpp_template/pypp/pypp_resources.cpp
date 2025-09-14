#include "pypp_resources.h"
#include "pypp_os.h"
#include "pypp_platform.h"

namespace pypp {
PyStr pypp_get_resource_dir() {
    PyStr exe_dir = platform::get_executable_dir();
    return os::path::join(exe_dir, PyStr(".."), PyStr(".."),
                          PyStr("resources"));
}
} // namespace pypp