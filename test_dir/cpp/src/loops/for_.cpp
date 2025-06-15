#include "loops\for_.h"

void for_loop_fn() {
    PyList<int> ret = PyList({-1});
    for (int i = 2; i < 10; i += 2) {
        ret.append(i);
    }
    ret.print();
}