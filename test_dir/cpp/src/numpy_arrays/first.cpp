#include "numpy_arrays\first.h"

void numpy_arrays_fn() {
    print(PyStr("NUMPY ARRAY RESULTS: "));
    NpArr<float> a = pypp_np::zeros<float>(PyList({2, 3}));
    print(a);
    NpArr<float> b = pypp_np::ones<float>(PyList({2, 3}));
    print(b);
    NpArr<float> c = pypp_np::full<float>(PyList({2, 3}), -1);
    print(c);
    print(pypp_np::zeros<double>(PyList({2, 3})));
    print(pypp_np::zeros<int16_t>(PyList({2, 3})));
    print(pypp_np::zeros<uint16_t>(PyList({2, 3})));
    print(pypp_np::zeros<int32_t>(PyList({2, 3})));
    print(pypp_np::zeros<uint64_t>(PyList({2, 3})));
    print(pypp_np::zeros<unsigned int>(PyList({2, 3})));
    print(pypp_np::zeros<long double>(PyList({2, 3})));
    print(pypp_np::zeros<bool>(PyList({2, 3})));
    print(pypp_np::ones<bool>(PyList({2, 3})));
    NpArr<double> d = pypp_np::array<double>(PyList({9.0, 10.0}));
    print(d);
    NpArr<double> e = pypp_np::array<double>(
        PyList({PyList({1.0, 2.0}), PyList({3.0, 4.0})}));
    print(e);
    NpArr<double> f = pypp_np::array<double>(
        PyList({PyList({PyList({1.0, 2.0}), PyList({3.0, 4.0})}),
                PyList({PyList({1.0, 2.0}), PyList({3.0, 99.0})})}));
    print(f);
    NpArr<double> g = pypp_np::array<double>(
        PyList({PyList({PyList({PyList({1.0, 2.0}), PyList({3.0, 4.0})}),
                        PyList({PyList({1.0, 2.0}), PyList({3.0, 99.0})})}),
                PyList({PyList({PyList({1.0, 2.0}), PyList({3.0, 4.0})}),
                        PyList({PyList({1.0, 2.0}), PyList({3.0, -77.0})})})}));
    print(g);
    double h = d(0) * 56.455432737426;
    print(to_pystr(h));
    double i = d(0);
    print(to_pystr(i));
    double j = d(0);
    print(to_pystr(j));
    double k = a(0, 0);
    print(to_pystr(k));
    float l1 = a(0, 0);
    print(to_pystr(l1));
    a.set(PyTup(0, 0), 1.0);
    print(a);
    a.set(PyTup(0, 0), 2);
    print(a);
}