#include "file_io/shutil_exceptions.h"
#include "exceptions/filesystem.h"
#include "py_str.h"
#include "pypp_os.h"
#include "pypp_resources.h"
#include "pypp_shutil.h"
#include "pypp_util/print.h"
#include "pypp_util/to_py_str.h"
#include <string>

namespace me {
void shutil_exceptions_fn() {
    pypp::print(pypp::PyStr("SHUTIL EXCEPTIONS RESULTS:"));
    pypp::PyStr resources_dir = pypp::res_dir();
    try {
        pypp::shutil::rmtree(pypp::os::path::join(
            resources_dir, pypp::PyStr("test_doesn't_exist")));
    } catch (const pypp::FileNotFoundError &pypp_pseudo_name_e) {
        std::string e = pypp_pseudo_name_e.msg_;
        pypp::print(pypp::PyStr("caught FileNotFoundError: "), e);
    }
    try {
        pypp::shutil::rmtree(pypp::os::path::join(
            resources_dir, pypp::PyStr("test_is_here.txt")));
    } catch (const pypp::NotADirectoryError &pypp_pseudo_name_e) {
        std::string e = pypp_pseudo_name_e.msg_;
        pypp::print(pypp::PyStr("caught NotADirectoryError: ") + pypp::str(e));
    }
}

} // namespace me