#pragma once

#include "py_dict.h"
#include "py_list.h"
#include "py_set.h"
#include "py_str.h"
#include <functional>

inline const int A = 1;
inline const pypp::PyStr B = pypp::PyStr("B");
inline const pypp::PyList<int> C({1, 2, 3});
inline const pypp::PyDict<int, int> D = {{0, 1}};
inline const pypp::PySet<int> E({1, 2, 3});
inline const std::function<int(int)> G = [](auto x) { return x + 1; };
struct _PseudoPyppNameMyConfig {
    int a = 1;
    pypp::PyStr b = pypp::PyStr("2");
};
inline _PseudoPyppNameMyConfig MyConfig;

struct _PseudoPyppNameMyConfig2 {
    pypp::PyStr a = pypp::PyStr("a");
    pypp::PyStr b = pypp::PyStr("b");
};
inline _PseudoPyppNameMyConfig2 MyConfig2;

void constant_fn();
inline const int F = 3;