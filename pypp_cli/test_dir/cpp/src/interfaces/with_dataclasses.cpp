#include "src/interfaces/with_dataclasses.h"
#include "pypp_util/print.h"

namespace me {
void GreeterImpl::greet(int a) {
    pypp::print(pypp::PyStr(std::format("{} says hello {} times!", name, a)));
}

void interface_with_dataclasses_fn() {
    pypp::print(pypp::PyStr("INTERFACE WITH DATACLASSES RESULTS:"));
    GreeterImpl g = GreeterImpl(pypp::PyStr("Alice"));
    g.greet(3);
}

} // namespace me