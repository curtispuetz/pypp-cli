#include "src/strings/f_strings.h"
#include "py_dict.h"
#include "py_list.h"
#include "py_range.h"
#include "py_set.h"
#include "py_str.h"
#include "py_tuple.h"
#include "pypp_util/print.h"
#include "slice/creators.h"
#include "slice/py_slice.h"

namespace me {
void f_strings_fn() {
    pypp::print(pypp::PyStr("F STRING RESULTS:"));
    pypp::PyStr a = pypp::PyStr(
        std::format("this {} my {}st test f string", pypp::PyStr("is"), 1));
    pypp::print(a);
    pypp::PySet<int> my_set({1, 2});
    pypp::PyDict<int, int> my_dict = {{0, 1}};
    pypp::PyStr b = pypp::PyStr(std::format(
        "list: {}, tuple: {}, set: {}, dict: {}, slice: {}, range: {}",
        pypp::PyList({1, 2}), pypp::PyTup(1, 2), my_set, my_dict,
        pypp::py_slice(10), pypp::PyRange(1)));
    pypp::print(b);
}

} // namespace me