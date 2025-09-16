#include "src/exceptions/test_all.h"
#include "exceptions/common.h"
#include "exceptions/exception.h"
#include "exceptions/filesystem.h"
#include "py_list.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include "pypp_util/to_py_str.h"
#include "src/exceptions/custom_exceptions.h"
#include <string>

namespace me {
void test_all_exceptions_fn() {
    pypp::print(pypp::PyStr("ALL EXCEPTIONS TEST RESULTS:"));
    pypp::PyList<pypp::Exception> exceptions(
        {pypp::Exception(pypp::PyStr("test")),
         pypp::ValueError(pypp::PyStr("test")),
         pypp::AssertionError(pypp::PyStr("test")),
         pypp::LookupError(pypp::PyStr("test")),
         pypp::IndexError(pypp::PyStr("test")),
         pypp::KeyError(pypp::PyStr("test")),
         pypp::RuntimeError(pypp::PyStr("test")),
         pypp::NotImplementedError(pypp::PyStr("test")),
         pypp::OSError(pypp::PyStr("test")),
         pypp::FileNotFoundError(pypp::PyStr("test")),
         pypp::NotADirectoryError(pypp::PyStr("test")),
         pypp::PermissionError(pypp::PyStr("test")),
         pypp::FileExistsError(pypp::PyStr("test"))});
    for (const auto &exc : exceptions) {
        try {
            throw exc;
        } catch (const pypp::Exception &pypp_pseudo_name_e) {
            std::string e = pypp_pseudo_name_e.msg_;
            pypp::print(pypp::PyStr("caught exception: ") + pypp::str(e));
        }
    }
    try {
        throw me::ChildException(pypp::PyStr("test"));
    } catch (const me::ChildException &pypp_pseudo_name_e) {
        std::string e = pypp_pseudo_name_e.msg_;
        pypp::print(pypp::PyStr("caught exception: ") + pypp::str(e));
    }
}

} // namespace me