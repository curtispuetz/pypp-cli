#include "numpy_arrays\first.h"

void numpy_arrays_fn() {
    PyStr("start of numpy arrays").print();
    NpArr<float> a = pypp_np::zeros<float>(PyList<size_t>({2, 3}));
    a.print();
    NpArr<float> b = pypp_np::ones<float>(PyList<size_t>({2, 3}));
    b.print();
    NpArr<float> c = pypp_np::full<float>(PyList<size_t>({2, 3}), -1);
    c.print();
    pypp_np::zeros<double>(PyList<size_t>({2, 3})).print();
    pypp_np::zeros<int16_t>(PyList<size_t>({2, 3})).print();
    pypp_np::zeros<uint16_t>(PyList<size_t>({2, 3})).print();
    pypp_np::zeros<int32_t>(PyList<size_t>({2, 3})).print();
    pypp_np::zeros<uint64_t>(PyList<size_t>({2, 3})).print();
    pypp_np::zeros<unsigned int>(PyList<size_t>({2, 3})).print();
    pypp_np::zeros<long double>(PyList<size_t>({2, 3})).print();
    pypp_np::zeros<bool>(PyList<size_t>({2, 3})).print();
    pypp_np::ones<bool>(PyList<size_t>({2, 3})).print();
}