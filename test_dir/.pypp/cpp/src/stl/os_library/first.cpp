#include "src/stl/os_library/first.h"
#include "py_str.h"
#include "py_tuple.h"
#include "pypp_assert.h"
#include "pypp_os.h"
#include "pypp_resources.h"
#include "pypp_text_io.h"
#include "pypp_util/print.h"

namespace me {
void os_library_fn() {
    pypp::print(pypp::PyStr("Running OS Library Test"));
    pypp::PyStr resources = pypp::res_dir();
    pypp::PyStr new_file = pypp::os::path::join(
        resources, pypp::PyStr("os_lib_results_new_file.txt"));
    pypp::assert(!pypp::os::path::exists(new_file), pypp::PyStr(""));
    {
        pypp::PyTextIO f(new_file, pypp::PyStr("w"));
        f.write(pypp::PyStr("Hello from os_library_fn!\n"));
    }
    pypp::assert(pypp::os::path::exists(new_file), pypp::PyStr(""));
    pypp::assert(pypp::os::path::isfile(new_file), pypp::PyStr(""));
    pypp::assert(!pypp::os::path::isfile(resources), pypp::PyStr(""));
    pypp::PyStr renamed_file = pypp::os::path::join(
        resources, pypp::PyStr("os_lib_results_renamed_file.txt"));
    pypp::os::rename(new_file, renamed_file);
    pypp::assert(!pypp::os::path::exists(new_file), pypp::PyStr(""));
    pypp::assert(pypp::os::path::exists(renamed_file), pypp::PyStr(""));
    pypp::os::remove(renamed_file);
    pypp::assert(!pypp::os::path::exists(renamed_file), pypp::PyStr(""));
    pypp::PyStr new_dir =
        pypp::os::path::join(resources, pypp::PyStr("os_lib_results_new_dir"));
    pypp::assert(!pypp::os::path::exists(new_dir), pypp::PyStr(""));
    pypp::os::mkdir(new_dir);
    pypp::assert(pypp::os::path::exists(new_dir), pypp::PyStr(""));
    pypp::assert(pypp::os::path::isdir(new_dir), pypp::PyStr(""));
    pypp::assert(!pypp::os::path::isdir(renamed_file), pypp::PyStr(""));
    pypp::os::rmdir(new_dir);
    pypp::assert(!pypp::os::path::exists(new_dir), pypp::PyStr(""));
    pypp::PyStr parent_dir = pypp::os::path::join(
        resources, pypp::PyStr("os_lib_results_new_nested_dir"));
    pypp::PyStr child_dir = pypp::os::path::join(parent_dir, pypp::PyStr("a"));
    pypp::assert(!pypp::os::path::exists(child_dir), pypp::PyStr(""));
    pypp::os::makedirs(child_dir);
    pypp::assert(pypp::os::path::exists(child_dir), pypp::PyStr(""));
    pypp::os::rmdir(child_dir);
    pypp::os::rmdir(parent_dir);
    pypp::assert(!pypp::os::path::exists(parent_dir), pypp::PyStr(""));
    pypp::PyStr dir_name = pypp::os::path::dirname(child_dir);
    pypp::assert(dir_name == parent_dir, pypp::PyStr(""));
    pypp::PyStr base_name = pypp::os::path::basename(child_dir);
    pypp::assert(base_name == pypp::PyStr("a"), pypp::PyStr(""));
    pypp::PyStr rel_path = pypp::os::path::join(
        resources, pypp::PyStr(".."), pypp::PyStr("some_relative_path"));
    pypp::PyStr abs_path = pypp::os::path::abspath(rel_path);
    pypp::assert(abs_path.endswith(pypp::PyStr("some_relative_path")),
                 pypp::PyStr(""));
    pypp::PyTup<pypp::PyStr, pypp::PyStr> split_path =
        pypp::os::path::split(child_dir);
    pypp::assert(split_path.get<0>() == parent_dir, pypp::PyStr(""));
    pypp::assert(split_path.get<1>() == pypp::PyStr("a"), pypp::PyStr(""));
    pypp::print(pypp::PyStr("OS Library Test Complete"));
}

} // namespace me