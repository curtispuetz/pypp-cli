#include "args_test.h"
#include "compy_util/print.h"

void int_arg(int a) { print(a); }

void float_arg(double a) { print(a); }

void str_arg(PyStr &a) { print(a); }

void bool_arg(bool a) { print(a); }

void float32_arg(float a) { print(a); }

void int8_t_arg(int8_t a) { print(a); }

void int16_t_arg(int16_t a) { print(a); }

void int32_t_arg(int32_t a) { print(a); }

void int64_t_arg(int64_t a) { print(a); }

void uint8_t_arg(uint8_t a) { print(a); }

void uint16_t_arg(uint16_t a) { print(a); }

void uint32_t_arg(uint32_t a) { print(a); }

void uint64_t_arg(uint64_t a) { print(a); }

void pseudo_int8_t_arg(pseudo_int8_t_cpp a) { print(a); }

void pseudo_int16_t_arg(pseudo_int16_t_cpp a) { print(a); }

void args_test_fn() {
    print(PyStr("compy ARGS TEST RESULTS:"));
    int a = 42;
    int_arg(a);
    double b = 3.14;
    float_arg(b);
    PyStr c = PyStr("Hello, World!");
    str_arg(c);
    bool d = true;
    bool_arg(d);
    float e = 1.23;
    float32_arg(e);
    int8_t f = 8;
    int8_t_arg(f);
    int16_t g = 16;
    int16_t_arg(g);
    int32_t h = 32;
    int32_t_arg(h);
    int64_t i = 64;
    int64_t_arg(i);
    uint8_t j = 8;
    uint8_t_arg(j);
    uint16_t k = 16;
    uint16_t_arg(k);
    uint32_t l = 32;
    uint32_t_arg(l);
    uint64_t m = 64;
    uint64_t_arg(m);
    pseudo_int8_t_cpp n = 8;
    pseudo_int8_t_arg(n);
    pseudo_int16_t_cpp o = 16;
    pseudo_int16_t_arg(o);
}
