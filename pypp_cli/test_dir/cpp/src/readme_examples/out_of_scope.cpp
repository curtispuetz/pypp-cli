#include "readme_examples/out_of_scope.h"
#include "pypp_util/print.h"

int var_out_of_scope(bool condition) {
    pypp::print(condition);
    return 1;
}
