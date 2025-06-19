#include "numpy_arrays\exceptions.h"

void numpy_array_exceptions_fn() {
    print(PyStr("NUMPY ARRAY EXCEPTIONS RESULTS:"));
    NpArr<float> a = pypp_np::zeros<float>(PyList({2, 3}));
    try {
        a(0, 0, 0);
    } catch (const PyppIndexError &pypp_e) {
        std::string e = pypp_e.what();
        print(PyStr("index error: ") + to_pystr(e));
    }
    try {
        a(99, 0);
    } catch (const PyppIndexError &pypp_e) {
        std::string e = pypp_e.what();
        print(PyStr("index error: ") + to_pystr(e));
    }
    try {
        a(0, 98);
    } catch (const PyppIndexError &pypp_e) {
        std::string e = pypp_e.what();
        print(PyStr("index error: ") + to_pystr(e));
    }
    PyList<int> empty_list = PyList<int>({});
    try {
        pypp_np::zeros<float>(empty_list);
    } catch (const PyppValueError &pypp_e) {
        std::string e = pypp_e.what();
        print(PyStr("value error: ") + to_pystr(e));
    }
    try {
        pypp_np::array<float>(empty_list);
    } catch (const PyppValueError &pypp_e) {
        std::string e = pypp_e.what();
        print(PyStr("value error: ") + to_pystr(e));
    }
    try {
        pypp_np::zeros<float>(PyList({-1, 2}));
    } catch (const PyppValueError &pypp_e) {
        std::string e = pypp_e.what();
        print(PyStr("value error: ") + to_pystr(e));
    }
    try {
        pypp_np::array<float>(PyList({PyList({1, 2}), PyList({3, 4, 5})}));
    } catch (const PyppValueError &pypp_e) {
        std::string e = pypp_e.what();
        print(PyStr("value error: ") + to_pystr(e));
    }
}