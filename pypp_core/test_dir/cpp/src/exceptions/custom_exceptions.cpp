#include "exceptions/custom_exceptions.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include "pypp_util/to_py_str.h"
#include <string>

class _PrivateCustomException : public PyppException {
  public:
    explicit _PrivateCustomException(const std::string &msg)
        : PyppException("_PrivateCustomException: " + msg) {}
};

void custom_exception_fn() {
    print(PyStr("PYPP CUSTOM EXCEPTION RESULTS:"));
    try {
        throw CustomException(
            PyStr("This is a custom exception message.").str());
    } catch (const CustomException &pypp_e) {
        std::string e = pypp_e.what();
        print(PyStr("custom exception caught: ") + to_pystr(e));
    }
    try {
        throw ChildException(PyStr("This is a child exception message.").str());
    } catch (const ChildException &pypp_e) {
        std::string e = pypp_e.what();
        print(PyStr("child exception caught: ") + to_pystr(e));
    }
}
