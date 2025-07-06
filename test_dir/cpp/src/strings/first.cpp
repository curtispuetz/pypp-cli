#include "strings\first.h"
#include "py_list.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include "pypp_util/to_py_str.h"
#include "slice/creators.h"
#include <utility>

void string_ops() {
    print(PyStr("STRING RESULTS:"));
    PyStr s = PyStr("  abd  ");
    print(s);
    print(to_pystr(s.len()));
    print(s[2]);
    print(s[py_slice(2, 4, 1)]);
    print(s[py_slice(0, 4, 1)]);
    print(s[py_slice(3, std::nullopt, 1)]);
    print(s[py_slice(2, 5, 2)]);
    print(s[py_slice(2, std::nullopt, 2)]);
    print(s[py_slice(0, std::nullopt, 1)]);
    print(PyStr("invalid slice: "));
    PyStr s_concat = PyStr("Hello ") + PyStr("World");
    print(s_concat);
    print(((PyStr("Hello") + PyStr(" ")) + PyStr("World")) + PyStr("!"));
    print(PyStr("A") + PyStr("B"));
    print(PyStr("AB") * 5);
    print(PyStr("ab").upper());
    print(PyStr("AB").lower());
    print(to_pystr(PyStr("abcdefg").find(PyStr("b"))));
    print(to_pystr(PyStr("abcbc").index(PyStr("bc"))));
    print(to_pystr(PyStr("abab").rindex(PyStr("ab"))));
    print(to_pystr(PyStr("ababab").count(PyStr("ab"))));
    print(to_pystr(PyStr("abab").startswith(PyStr("ab"))));
    print(to_pystr(PyStr("abab").endswith(PyStr("ab"))));
    print(PyStr("abcdab").replace(PyStr("ab"), PyStr("xy")));
    print(PyStr("abcdab").replace(PyStr("ab"), PyStr("xy"), 1));
    print(s.strip());
    print(s.lstrip());
    print(s.rstrip());
    print(to_pystr(PyStr("a") == PyStr("a")));
    print(to_pystr(PyStr("a") > PyStr("a")));
    print(to_pystr(PyStr("a") >= PyStr("a")));
    print(to_pystr(PyStr("a") < PyStr("a")));
    print(to_pystr(PyStr("a") <= PyStr("a")));
    print(to_pystr(PyStr("a") != PyStr("a")));
    print(s);
    s += PyStr("n");
    s += PyStr("");
    print(s);
    s *= 5;
    print(s);
    s *= -5;
    print(s);
    PyList<PyStr> l1 = PyStr("0,1,2").split(PyStr(","));
    print(l1);
    PyList<PyStr> l2 = PyStr("0 1 2").split();
    print(l2);
    print(PyStr(" ").join(PyList({PyStr("1"), PyStr("2"), PyStr("3")})));
    PyStr s_joined = PyStr(", ").join(
        PyList({PyStr("a"), PyStr("b"), PyStr("c"), PyStr("d")}));
    print(s_joined);
    PyStr a = PyStr("");
    print(a);
    PyList<PyStr> list_of_chars = PyList<PyStr>({});
    for (const auto &c : PyStr("abcdefg")) {
        PyStr ch = c;
        list_of_chars.append(std::move(ch));
    }
    print(list_of_chars);
}