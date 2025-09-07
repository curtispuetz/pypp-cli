#include "loops/while_.h"
#include "py_list.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include <utility>

namespace me {
void while_loop_fn() {
    pypp::print(pypp::PyStr("WHILE LOOP RESULTS:"));
    pypp::PyList<int> a({});
    int i = 0;
    while (i < 3) {
        a.append(std::move(i));
        i += 1;
    }
    pypp::print(a);
    while (true) {
        a.append(std::move(i));
        if (i > 3) {
            break;
        }
        i += 1;
    }
    pypp::print(a);
    while (i < 7) {
        if (i == 5) {
            i += 1;
            continue;
        }
        a.append(std::move(i));
        i += 1;
    }
    pypp::print(a);
}

} // namespace me