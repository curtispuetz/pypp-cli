#include "slices/first.h"
#include "py_list.h"
#include "py_set.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include "slice/creators.h"
#include "slice/py_slice.h"

namespace me {
void slices_fn() {
    pypp::print(pypp::PyStr("SLICE RESULTS:"));
    pypp::print(pypp::py_slice(2));
    pypp::print(pypp::py_slice(1, 5));
    pypp::print(pypp::py_slice(1, 5, -2));
    pypp::print(pypp::py_slice(1, 5, 1));
    pypp::print(pypp::py_slice(0, 5, 1));
    pypp::PyList<int> a({1, 2, 3, 4, 5});
    pypp::PyStr s = pypp::PyStr("12345");
    pypp::PySlice b = pypp::py_slice(2);
    pypp::print(a[b]);
    pypp::print(a[pypp::py_slice(0, 2, 1)]);
    pypp::print(s[b]);
    pypp::print(s[pypp::py_slice(0, 2, 1)]);
    pypp::PySlice c = pypp::py_slice(1, 4);
    pypp::print(a[c]);
    pypp::print(a[pypp::py_slice(1, 4, 1)]);
    pypp::print(s[c]);
    pypp::print(s[pypp::py_slice(1, 4, 1)]);
    pypp::PySlice d = pypp::py_slice(4, 1, -1);
    pypp::print(a[d]);
    pypp::print(a[pypp::py_slice(4, 1, -1)]);
    pypp::print(s[d]);
    pypp::print(s[pypp::py_slice(4, 1, -1)]);
    pypp::PySlice e = pypp::py_slice(0, 100, 2);
    pypp::print(a[e]);
    pypp::print(a[pypp::py_slice(0, std::nullopt, 2)]);
    pypp::print(s[e]);
    pypp::print(s[pypp::py_slice(0, std::nullopt, 2)]);
    pypp::PySlice f = pypp::py_slice(2, 100);
    pypp::print(a[f]);
    pypp::print(a[pypp::py_slice(2, std::nullopt, 1)]);
    pypp::print(s[f]);
    pypp::print(s[pypp::py_slice(2, std::nullopt, 1)]);
    pypp::PySlice g = pypp::py_slice(2, 100, 2);
    pypp::print(a[g]);
    pypp::print(a[pypp::py_slice(2, std::nullopt, 2)]);
    pypp::print(s[g]);
    pypp::print(s[pypp::py_slice(2, std::nullopt, 2)]);
    pypp::PySet<pypp::PySlice> h({e, g});
    pypp::print(h);
}

} // namespace me