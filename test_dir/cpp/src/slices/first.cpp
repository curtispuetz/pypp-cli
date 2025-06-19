#include "slices\first.h"

void slices_fn() {
    print(PyStr("SLICE RESULTS:"));
    print(PySlice(2));
    print(PySlice(1, 5));
    print(PySlice(1, 5, -2));
    print(PySlice(1, 5, 1));
    print(PySlice(0, 5, 1));
}