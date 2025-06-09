#pragma once

template<typename T>
struct is_pystr {
    static constexpr bool value = false;
};
