#include "constants.h"
#include "pypp_util/print.h"

const int _A = 2;
void constant_fn() {
    print(PyStr("CONSTANT RESULTS:"));
    const int _F = 4;
    print(F);
    print(_F);
    print(G(1));
}
