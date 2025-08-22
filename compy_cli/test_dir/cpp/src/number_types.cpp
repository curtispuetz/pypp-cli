#include "number_types.h"
#include "compy_util/print.h"
#include "py_str.h"
#include <cstdint>

void number_types_fn() {
    print(PyStr("NUMBER TYPES RESULTS:"));
    int8_t a = -1;
    int16_t b = -129;
    int32_t c = -32769;
    int64_t d = -2147483649;
    uint8_t e = 1;
    uint16_t f = 256;
    uint32_t g = 65536;
    uint64_t h = 4294967296;
    print(a, b, c, d, e, f, g, h);
    float i = 3.14;
    print(i);
}
