#include "exceptions/test_all.h"
#include "exceptions/common.h"
#include "exceptions/custom_exceptions.h"
#include "exceptions/exception.h"
#include "py_list.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include "pypp_util/to_py_str.h"
#include <string>

namespace me {
void test_all_exceptions_fn() {
    pypp::print(pypp::PyStr("ALL EXCEPTIONS TEST RESULTS:"));
    pypp::PyList<pypp::Exception> exceptions(
        {pypp::Exception(pypp::PyStr("test")),
         pypp::ValueError(pypp::PyStr("test"))});
    for (const auto &exc : exceptions) {
        try {
            throw exc;
        } catch (const pypp::Exception &pypp_e) {
            std::string e = pypp_e.what();
            pypp::print(pypp::PyStr("caught exception: ") + pypp::str(e));
        }
    }
    try {
        throw me::ChildException(pypp::PyStr("test"));
    } catch (const me::ChildException &pypp_e) {
        std::string e = pypp_e.what();
        pypp::print(pypp::PyStr("caught exception: ") + pypp::str(e));
    }
}

} // namespace me