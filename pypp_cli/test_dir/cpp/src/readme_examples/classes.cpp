#include "readme_examples/classes.h"

pypp::PyStr Greeter::greet() {
    return pypp::PyStr(std::format("Hello, {} {}!", prefix, name));
}
