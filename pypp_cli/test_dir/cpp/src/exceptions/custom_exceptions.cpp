#include "exceptions/custom_exceptions.h"
#include "pypp_util/print.h"
#include "pypp_util/to_py_str.h"
#include <string>

namespace me {
class _PrivateCustomException : public pypp::PyppException {
  public:
    explicit _PrivateCustomException(const pypp::PyStr &msg)
        : pypp::PyppException(pypp::PyStr("_PrivateCustomException: ") + msg) {}
};

void custom_exception_fn() {
    pypp::print(pypp::PyStr("pypp CUSTOM EXCEPTION RESULTS:"));
    try {
        throw CustomException(
            pypp::PyStr("This is a custom exception message."));
    } catch (const CustomException &pypp_e) {
        std::string e = pypp_e.what();
        pypp::print(pypp::PyStr("custom exception caught: ") +
                    pypp::to_pystr(e));
    }
    try {
        throw ChildException(pypp::PyStr("This is a child exception message."));
    } catch (const ChildException &pypp_e) {
        std::string e = pypp_e.what();
        pypp::print(pypp::PyStr("child exception caught: ") +
                    pypp::to_pystr(e));
    }
}

} // namespace me