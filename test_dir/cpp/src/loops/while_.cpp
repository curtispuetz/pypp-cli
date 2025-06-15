#include "loops\while_.h"

void while_loop_fn() {
    PyList<int> a = PyList<int>({});
    int i = 0;
    while (i < 3) {
        a.append(i);
        i += 1;
    }
    a.print();
    while (true) {
        a.append(i);
        if (i > 3) {
            break;
        }
        i += 1;
    }
    a.print();
    while (i < 7) {
        if (i == 5) {
            i += 1;
            continue;
        }
        a.append(i);
        i += 1;
    }
    a.print();
}