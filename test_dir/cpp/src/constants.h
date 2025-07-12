#pragma once

#include "py_dict.h"
#include "py_list.h"
#include "py_set.h"
#include "py_str.h"
#include <functional>

inline const int A = 1;
inline const PyStr B = PyStr("B");
inline const PyList<int> C = PyList({1, 2, 3});
inline const PyDict<int, int> D({{0, 1}});
inline const PySet<int> E = PySet({1, 2, 3});
inline const std::function<int(int)> G = [](auto x) { return x + 1; };
struct _PseudoPyppNameMyConfig {
    int a = 1;
    PyStr b = PyStr("2");
};
inline _PseudoPyppNameMyConfig MyConfig;
struct _PseudoPyppNameMyConfig2 {
    PyStr a = PyStr("a");
    PyStr b = PyStr("b");
};
inline _PseudoPyppNameMyConfig2 MyConfig2;
void constant_fn();
inline const int F = 3;