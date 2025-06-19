#pragma once

#include "py_str.h"

// TODO later: Use this when printing in collections (it looks way better). But
// it is a little tricky to set this up
PyStr escape_specials(const PyStr &input);