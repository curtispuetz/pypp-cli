#include "readme_examples/dataclasses.h"

pypp::PyStr Greeter::greet() {
    return pypp::PyStr(std::format("Hello, {} {}!", prefix, name));
}
