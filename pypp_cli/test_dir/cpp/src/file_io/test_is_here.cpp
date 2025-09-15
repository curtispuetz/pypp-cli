#include "src/file_io/test_is_here.h"
#include "exceptions/exception.h"
#include "py_str.h"
#include "pypp_os.h"
#include "pypp_resources.h"
#include "pypp_util/print.h"

namespace me {
void test_is_here_fn() {
    pypp::print(pypp::PyStr("FILE IO TEST IS HERE RESULTS:"));
    pypp::PyStr resources_dir = pypp::res_dir();
    pypp::PyStr file =
        pypp::os::path::join(resources_dir, pypp::PyStr("test_is_here.txt"));
    if (pypp::os::path::isfile(file)) {
        pypp::print(pypp::PyStr("test_is_here.txt file exists"));
    } else {
        throw pypp::Exception(
            pypp::PyStr("test_is_here.txt file does not exist"));
    }
}

} // namespace me