#include "strings/first.h"
#include "py_list.h"
#include "py_str.h"
#include "pypp_util/print.h"
#include "pypp_util/to_py_str.h"
#include "slice/creators.h"
#include <utility>

namespace me {
void string_ops() {
    pypp::print(pypp::PyStr("STRING RESULTS:"));
    pypp::PyStr s = pypp::PyStr("  abd  ");
    pypp::print(s);
    pypp::print(pypp::str(s.len()));
    pypp::print(s[2]);
    pypp::print(s[pypp::py_slice(2, 4, 1)]);
    pypp::print(s[pypp::py_slice(0, 4, 1)]);
    pypp::print(s[pypp::py_slice(3, std::nullopt, 1)]);
    pypp::print(s[pypp::py_slice(2, 5, 2)]);
    pypp::print(s[pypp::py_slice(2, std::nullopt, 2)]);
    pypp::print(s[pypp::py_slice(0, std::nullopt, 1)]);
    pypp::print(pypp::PyStr("invalid slice: "));
    pypp::PyStr s_concat = pypp::PyStr("Hello ") + pypp::PyStr("World");
    pypp::print(s_concat);
    pypp::print(
        ((pypp::PyStr("Hello") + pypp::PyStr(" ")) + pypp::PyStr("World")) +
        pypp::PyStr("!"));
    pypp::print(pypp::PyStr("A") + pypp::PyStr("B"));
    pypp::print(pypp::PyStr("AB") * 5);
    pypp::print(pypp::PyStr("ab").upper());
    pypp::print(pypp::PyStr("AB").lower());
    pypp::print(pypp::str(pypp::PyStr("abcdefg").find(pypp::PyStr("b"))));
    pypp::print(pypp::str(pypp::PyStr("abcbc").index(pypp::PyStr("bc"))));
    pypp::print(pypp::str(pypp::PyStr("abab").rindex(pypp::PyStr("ab"))));
    pypp::print(pypp::str(pypp::PyStr("ababab").count(pypp::PyStr("ab"))));
    pypp::print(pypp::str(pypp::PyStr("abab").startswith(pypp::PyStr("ab"))));
    pypp::print(pypp::str(pypp::PyStr("abab").endswith(pypp::PyStr("ab"))));
    pypp::print(
        pypp::PyStr("abcdab").replace(pypp::PyStr("ab"), pypp::PyStr("xy")));
    pypp::print(
        pypp::PyStr("abcdab").replace(pypp::PyStr("ab"), pypp::PyStr("xy"), 1));
    pypp::print(s.strip());
    pypp::print(s.lstrip());
    pypp::print(s.rstrip());
    pypp::print(pypp::str(pypp::PyStr("a") == pypp::PyStr("a")));
    pypp::print(pypp::str(pypp::PyStr("a") > pypp::PyStr("a")));
    pypp::print(pypp::str(pypp::PyStr("a") >= pypp::PyStr("a")));
    pypp::print(pypp::str(pypp::PyStr("a") < pypp::PyStr("a")));
    pypp::print(pypp::str(pypp::PyStr("a") <= pypp::PyStr("a")));
    pypp::print(pypp::str(pypp::PyStr("a") != pypp::PyStr("a")));
    pypp::print(s);
    s += pypp::PyStr("n");
    s += pypp::PyStr("");
    pypp::print(s);
    s *= 5;
    pypp::print(s);
    s *= -5;
    pypp::print(s);
    pypp::PyList<pypp::PyStr> l1 = pypp::PyStr("0,1,2").split(pypp::PyStr(","));
    pypp::print(l1);
    pypp::PyList<pypp::PyStr> l2 = pypp::PyStr("0 1 2").split();
    pypp::print(l2);
    pypp::print(pypp::PyStr(" ").join(
        pypp::PyList({pypp::PyStr("1"), pypp::PyStr("2"), pypp::PyStr("3")})));
    pypp::PyStr s_joined = pypp::PyStr(", ").join(
        pypp::PyList({pypp::PyStr("a"), pypp::PyStr("b"), pypp::PyStr("c"),
                      pypp::PyStr("d")}));
    pypp::print(s_joined);
    pypp::PyStr a = pypp::PyStr("");
    pypp::print(a);
    pypp::PyList<pypp::PyStr> list_of_chars({});
    for (const auto &c : pypp::PyStr("abcdefg")) {
        pypp::PyStr ch = c;
        list_of_chars.append(std::move(ch));
    }
    pypp::print(list_of_chars);
    pypp::PyStr m = pypp::PyStr("abc");
    if (m.contains(pypp::PyStr("a"))) {
        pypp::print(pypp::PyStr(std::format("a in {}", m)));
    }
    if (!m.contains(pypp::PyStr("d"))) {
        pypp::print(pypp::PyStr(std::format("d not in {}", m)));
    }
    pypp::print(m.max());
    pypp::print(m.min());
}

} // namespace me