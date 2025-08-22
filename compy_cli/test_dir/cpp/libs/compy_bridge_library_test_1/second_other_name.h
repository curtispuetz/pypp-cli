#pragma once

// inline because another library defines a function
// with this same name so if there was no inline then
// it would result in a linking error.
inline int pseudo_fn_a()
{
    return 43;
}