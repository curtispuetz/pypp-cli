#include "pypp_platform.h"
#include <filesystem>

#ifdef _WIN32
#include <windows.h>
#elif __linux__
#include <unistd.h>
#elif __APPLE__
#include <mach-o/dyld.h>
#include <vector>
#endif

#include <exceptions/stdexcept.h> // Only needed in the implementation

namespace platform {

PyStr get_executable_dir() {
#ifdef _WIN32
    wchar_t path[MAX_PATH] = {0};
    GetModuleFileNameW(NULL, path, MAX_PATH);
    return PyStr(std::filesystem::path(path).parent_path().string());
#elif __linux__
    char result[PATH_MAX];
    ssize_t count = readlink("/proc/self/exe", result, PATH_MAX);
    if (count > 0) {
        return PyStr(std::filesystem::path(result).parent_path().string());
    }
#elif __APPLE__
    char raw_path_name[PATH_MAX];
    char real_path_name[PATH_MAX];
    uint32_t raw_path_size = (uint32_t)sizeof(raw_path_name);

    if (!_NSGetExecutablePath(raw_path_name, &raw_path_size)) {
        realpath(raw_path_name, real_path_name);
        return PyStr(
            std::filesystem::path(real_path_name).parent_path().string());
    }
#endif
    throw PyppRuntimeError("Could not determine executable directory");
}

} // namespace platform
