#include "readme_examples/classes.h"

namespace me {
pypp::PyStr Greeter::greet() {
    return pypp::PyStr(std::format("Hello, {} {}!", prefix, name));
}

} // namespace me