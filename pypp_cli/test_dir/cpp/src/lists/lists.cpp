#include "lists/lists.h"
#include "py_list.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include "pypp_util/to_py_str.h"
#include "slice/creators.h"
#include <utility>

namespace me {
void _test_fn(pypp::PyList<pypp::PyStr> arg1) { pypp::print(arg1); }

void list_fn() {
    pypp::print(pypp::PyStr("LIST RESULTS:"));
    pypp::PyList<int> a({1, 2, 3, 4, 5});
    pypp::print(a);
    a[0] = 10;
    pypp::print(a);
    a.append(11);
    pypp::print(a);
    pypp::print(pypp::to_pystr(a[-1]));
    int b = a[-1];
    pypp::print(pypp::to_pystr(b));
    b = 20;
    pypp::print(pypp::to_pystr(b));
    pypp::print(a);
    pypp::print(pypp::to_pystr(a.len()));
    a.reverse();
    pypp::print(a);
    pypp::print(pypp::to_pystr(a.count(2)));
    pypp::print(pypp::to_pystr(a.index(2)));
    a.remove(2);
    pypp::print(a);
    a.insert(4, 2);
    pypp::print(a);
    int ins_val = 2;
    a.insert(4, std::move(ins_val));
    pypp::print(a);
    int popped_val = a.pop();
    pypp::print(pypp::to_pystr(popped_val));
    pypp::print(a);
    int popped_val2 = a.pop(1);
    pypp::print(pypp::to_pystr(popped_val2));
    pypp::print(a);
    a.clear();
    pypp::print(a);
    pypp::print(pypp::to_pystr(pypp::PyList({1, 2}) == pypp::PyList({1, 2})));
    pypp::print(pypp::to_pystr(pypp::PyList({1, 2}) < pypp::PyList({1, 2})));
    pypp::print(pypp::to_pystr(pypp::PyList({1, 2}) <= pypp::PyList({1, 2})));
    pypp::print(pypp::to_pystr(pypp::PyList({1, 2}) > pypp::PyList({1, 2})));
    pypp::print(pypp::to_pystr(pypp::PyList({1, 2}) >= pypp::PyList({1, 2})));
    pypp::print(pypp::to_pystr(pypp::PyList({1, 2}) != pypp::PyList({1, 2})));
    pypp::PyList<int> c = pypp::PyList({1, 2}) + pypp::PyList({3, 4});
    pypp::print(c);
    c += pypp::PyList({5, 6});
    pypp::print(c);
    pypp::PyList<int> d = c * 3;
    pypp::print(d);
    c *= 3;
    pypp::print(c);
    pypp::print(c[pypp::py_slice(1, 4, 1)]);
    pypp::print(c[pypp::py_slice(1, c.len() - 1, 2)]);
    pypp::print(c[pypp::py_slice(1, std::nullopt, 2)]);
    pypp::print(c[pypp::py_slice(1, std::nullopt, 1)]);
    pypp::print(c[pypp::py_slice(0, 4, 1)]);
    pypp::print(c[pypp::py_slice(0, std::nullopt, 2)]);
    pypp::print(c[pypp::py_slice(0, std::nullopt, 1)]);
    pypp::print(c[pypp::py_slice(c.len() - 2, 5, 1)]);
    pypp::print(c[pypp::py_slice(c.len() - 4, c.len() - 1, 1)]);
    pypp::print(c[pypp::py_slice(5, 1, -1)]);
    pypp::PyList<pypp::PyStr> e({pypp::PyStr("a"), pypp::PyStr("b")});
    pypp::print(e);
    pypp::PyList<int> f({});
    pypp::print(f);
    e.reserve(10);
    pypp::PyList<pypp::PyList<int>> g(
        {pypp::PyList({1, 2}), pypp::PyList({3, 4})});
    pypp::PyList<int> &g_0 = g[0];
    g_0.append(99);
    pypp::print(g);
    g[1].append(98);
    pypp::print(g);
    _test_fn(pypp::PyList({pypp::PyStr("1"), pypp::PyStr("2")}));
    e.extend(pypp::PyList({pypp::PyStr("c"), pypp::PyStr("d")}));
    pypp::print(e);
    pypp::PyList<pypp::PyStr> h({pypp::PyStr("e"), pypp::PyStr("f")});
    e.extend(std::move(h));
    pypp::print(e);
    pypp::PyList<int> i({5, 3, 1, 4, 2});
    i.sort();
    pypp::print(i);
    pypp::PyList<int> j = i[pypp::py_slice(0, std::nullopt, 1)];
    j[1] = 99;
    pypp::print(i);
    pypp::print(j);
}

} // namespace me