#pragma once

#include "py_str.h"
#include <cstdint>

void int_arg(int a);
void float_arg(double a);
void str_arg(PyStr &a);
void bool_arg(bool a);
void float32_arg(float a);
void int8_t_arg(int8_t a);
void int16_t_arg(int16_t a);
void int32_t_arg(int32_t a);
void int64_t_arg(int64_t a);
void uint8_t_arg(uint8_t a);
void uint16_t_arg(uint16_t a);
void uint32_t_arg(uint32_t a);
void uint64_t_arg(uint64_t a);