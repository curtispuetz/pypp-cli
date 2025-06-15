#include "loops\while_.h"

void while_loop_fn() {
    PyList<int> a = PyList<int>({});
    int i = 0;
    while (i < 3) {
        a.append(i);
        i += 1;
    }
    a.print();
}