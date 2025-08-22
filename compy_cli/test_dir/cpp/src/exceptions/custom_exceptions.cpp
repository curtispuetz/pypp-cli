#include "exceptions/custom_exceptions.h"
#include "compy_util/print.h"
#include "compy_util/to_py_str.h"
#include "py_str.h"
#include <string>

class _PrivateCustomException : public CompyException {
  public:
    explicit _PrivateCustomException(const std::string &msg)
        : CompyException("_PrivateCustomException: " + msg) {}
};

void custom_exception_fn() {
    print(PyStr("compy CUSTOM EXCEPTION RESULTS:"));
    try {
        throw CustomException(
            PyStr("This is a custom exception message.").str());
    } catch (const CustomException &compy_e) {
        std::string e = compy_e.what();
        print(PyStr("custom exception caught: ") + to_pystr(e));
    }
    try {
        throw ChildException(PyStr("This is a child exception message.").str());
    } catch (const ChildException &compy_e) {
        std::string e = compy_e.what();
        print(PyStr("child exception caught: ") + to_pystr(e));
    }
}
