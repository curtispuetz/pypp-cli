#include "loops\while_.h"
#include "py_list.h"
#include "py_str.h"
#include "pypp_util/print.h"

void while_loop_fn() {
    print(PyStr("WHILE LOOP RESULTS:"));
    PyList<int> a = PyList<int>({});
    int i = 0;
    while (i < 3) {
        a.append(i);
        i += 1;
    }
    print(a);
    while (true) {
        a.append(i);
        if (i > 3) {
            break;
        }
        i += 1;
    }
    print(a);
    while (i < 7) {
        if (i == 5) {
            i += 1;
            continue;
        }
        a.append(i);
        i += 1;
    }
    print(a);
}