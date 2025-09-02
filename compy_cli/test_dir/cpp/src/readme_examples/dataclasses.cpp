#include "readme_examples/dataclasses.h"

PyStr Greeter::greet() {
    return PyStr(std::format("Hello, {} {}!", prefix, name));
}
