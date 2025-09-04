#include "readme_examples/classes.h"

PyStr Greeter::greet() {
    return PyStr(std::format("Hello, {} {}!", prefix, name));
}
