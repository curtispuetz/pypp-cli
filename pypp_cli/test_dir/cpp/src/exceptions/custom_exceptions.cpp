#include "src/exceptions/custom_exceptions.h"
#include "pypp_util/print.h"
#include "pypp_util/to_py_str.h"
#include <string>

namespace me {
class _PrivateCustomException : public pypp::Exception {
  public:
    explicit _PrivateCustomException(const pypp::PyStr &msg)
        : pypp::Exception(pypp::PyStr("_PrivateCustomException: ") + msg) {}
};

void custom_exception_fn() {
    pypp::print(pypp::PyStr("pypp CUSTOM EXCEPTION RESULTS:"));
    try {
        throw CustomException(
            pypp::PyStr("This is a custom exception message."));
    } catch (const CustomException &pypp_pseudo_name_e) {
        std::string e = pypp_pseudo_name_e.msg_;
        pypp::print(pypp::PyStr("custom exception caught: ") + pypp::str(e));
    }
    try {
        throw ChildException(pypp::PyStr("This is a child exception message."));
    } catch (const ChildException &pypp_pseudo_name_e) {
        std::string e = pypp_pseudo_name_e.msg_;
        pypp::print(pypp::PyStr("child exception caught: ") + pypp::str(e));
    }
    try {
        throw CustomValueError(
            pypp::PyStr("This is a custom value error message."));
    } catch (const pypp::ValueError &pypp_pseudo_name_e) {
        std::string e = pypp_pseudo_name_e.msg_;
        pypp::print(pypp::PyStr("custom value error caught: ") + pypp::str(e));
    }
}

} // namespace me