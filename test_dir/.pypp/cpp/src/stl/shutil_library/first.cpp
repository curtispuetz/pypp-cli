#include "src/stl/shutil_library/first.h"
#include "py_str.h"
#include "pypp_assert.h"
#include "pypp_os.h"
#include "pypp_resources.h"
#include "pypp_shutil.h"
#include "pypp_text_io.h"
#include "pypp_util/print.h"

namespace me {
void shutil_library_fn() {
    pypp::print(pypp::PyStr("Running SHUTIL Library Test"));
    pypp::PyStr resources = pypp::res_dir();
    pypp::PyStr new_dir = pypp::os::path::join(
        resources, pypp::PyStr("shutil_lib_results_new_dir"));
    pypp::os::mkdir(new_dir);
    pypp::PyStr new_file = pypp::os::path::join(new_dir, pypp::PyStr("a.txt"));
    {
        pypp::PyTextIO f(new_file, pypp::PyStr("w"));
        f.write(pypp::PyStr("Hello from shutil_library_fn!\n"));
    }
    pypp::assert(pypp::os::path::exists(new_dir), pypp::PyStr(""));
    pypp::shutil::rmtree(new_dir);
    pypp::assert(!pypp::os::path::exists(new_dir), pypp::PyStr(""));
    pypp::print(pypp::PyStr("SHUTIL Library Test Passed"));
}

} // namespace me