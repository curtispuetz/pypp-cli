#include "loops/while_.h"
#include "compy_util/print.h"
#include "py_list.h"
#include "py_str.h"
#include <utility>

void while_loop_fn() {
    print(PyStr("WHILE LOOP RESULTS:"));
    PyList<int> a = PyList<int>({});
    int i = 0;
    while (i < 3) {
        a.append(std::move(i));
        i += 1;
    }
    print(a);
    while (true) {
        a.append(std::move(i));
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
        a.append(std::move(i));
        i += 1;
    }
    print(a);
}
