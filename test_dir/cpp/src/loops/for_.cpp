#include "loops\for_.h"

void for_loop_fn() {
    PyList<int> ret = PyList<int>({});
    for (int i = 2; i < 10; i += 2) {
        ret.append(i);
    }
    ret.print();
    PyList<int> a = PyList<int>({});
    for (auto val : ret) {
        a.append(val);
    }
    a.print();
    PySet<int> b = PySet({10, 20, 30});
    for (auto val : b) {
        a.append(val);
    }
    a.print();
}