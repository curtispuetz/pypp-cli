#include "src/readme_examples/not_out_of_scope.h"

namespace me {
int var_not_out_of_scope(bool condition) {
    int m;
    if (condition) {
        m = 42;
    } else {
        m = 100;
    }
    return 10 * m;
}

} // namespace me