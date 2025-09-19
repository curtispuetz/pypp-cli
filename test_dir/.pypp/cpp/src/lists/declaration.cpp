#include "src/lists/declaration.h"
#include "py_list.h"
#include "py_str.h"
#include "pypp_util/print.h"

namespace me {
void list_declaration_fn() {
    pypp::print(pypp::PyStr("LIST DECLARATION RESULTS:"));
    pypp::PyList<int> a({});
    pypp::print(a);
    pypp::PyList<int> b({1, 2, 3, 4, 5});
    pypp::print(b);
    pypp::PyList<int> c = pypp::PyList({1, 2, 3}) * 5;
    pypp::print(c);
    pypp::PyList<int> d(10);
    pypp::print(d);
    pypp::PyList<double> e(5);
    pypp::print(e);
    pypp::PyList<pypp::PyStr> f(3);
    pypp::print(f);
    pypp::PyList<int> g(10, 99);
    pypp::print(g);
    pypp::PyList<double> h(5, 1.1);
    pypp::print(h);
    pypp::PyList<pypp::PyStr> i(3, pypp::PyStr("hello"));
    pypp::print(i);
}

} // namespace me