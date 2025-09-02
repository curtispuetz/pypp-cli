#include "readme_examples/not_out_of_scope.h"

int var_not_out_of_scope(bool condition) {
    int m;
    if (condition) {
        m = 42;
    } else {
        m = 100;
    }
    return 10 * m;
}
