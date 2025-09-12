#include "built_in_functions/number_conversions.h"
#include "py_str.h"
#include "pypp_util/create/cstdint.h"
#include "pypp_util/create/others.h"
#include "pypp_util/print.h"
#include <cstdint>

namespace me {
void number_conversions_fn() {
    pypp::print(pypp::PyStr("NUMBER CONVERSIONS RESULTS:"));
    pypp::PyStr a = pypp::PyStr("123");
    pypp::PyStr b = pypp::PyStr("45.67");
    int a_int = pypp::int_(a);
    double b_float = pypp::float_(b);
    float b_float32 = pypp::to_float32(b_float);
    bool a_bool = pypp::bool_(a_int);
    pypp::print(pypp::PyStr(
        std::format("int(a): {}, float(b): {}, float32(b): {}, bool(a): {}",
                    a_int, b_float, b_float32, a_bool)));
    double a_float = pypp::float_(a_int);
    float a_float32 = pypp::to_float32(a_float);
    int b_int = pypp::int_(b_float);
    bool b_bool = pypp::bool_(b_float);
    pypp::print(pypp::PyStr(
        std::format("float(a): {}, float32(a): {}, int(b): {}, bool(b): {}",
                    a_float, a_float32, b_int, b_bool)));
    int8_t a_int8_t = pypp::to_int8_t(257);
    int16_t a_int16_t = pypp::to_int16_t(a_int);
    int32_t a_int32_t = pypp::to_int32_t(a_int);
    int64_t a_int64_t = pypp::to_int64_t(a_int);
    uint8_t a_uint8_t = pypp::to_uint8_t(a_int);
    uint16_t a_uint16_t = pypp::to_uint16_t(a_int);
    uint32_t a_uint32_t = pypp::to_uint32_t(a_int);
    uint64_t a_uint64_t = pypp::to_uint64_t(a_int);
    pypp::print(pypp::PyStr(
        std::format("int8_t: {}, int16_t: {}, int32_t: {}, int64_t: {}, "
                    "uint8_t: {}, uint16_t: {}, uint32_t: {}, uint64_t: {}",
                    a_int8_t, a_int16_t, a_int32_t, a_int64_t, a_uint8_t,
                    a_uint16_t, a_uint32_t, a_uint64_t)));
}

} // namespace me