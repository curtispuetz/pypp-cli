#include <array>
#include <cstddef>
#include <iostream>
#include <type_traits>
#include <initializer_list>

// Forward declaration
template<typename T, size_t... Dims>
class MultiArray;


// Base case
template<typename T, size_t LastDim>
class MultiArray<T, LastDim> {
public:
    using Storage = std::array<T, LastDim>;
    Storage data;

    T& operator[](size_t idx) {
        return data[idx];
    }

    const T& operator[](size_t idx) const {
        return data[idx];
    }

    constexpr std::array<size_t, 1> shape() const {
        return {LastDim};
    }

    // Example method: all()
    bool all() const {
        for (const auto& val : data) {
            if (!val) return false;
        }
        return true;
    }

    // Example method: any()
    bool any() const {
        for (const auto& val : data) {
            if (val) return true;
        }
        return false;
    }
};


// Recursive case
template<typename T, size_t FirstDim, size_t... RestDims>
class MultiArray<T, FirstDim, RestDims...> {
public:
    using SubArray = MultiArray<T, RestDims...>;
    using Storage = std::array<SubArray, FirstDim>;

    Storage data;

    SubArray& operator[](size_t idx) {
        return data[idx];
    }

    const SubArray& operator[](size_t idx) const {
        return data[idx];
    }

    constexpr std::array<size_t, sizeof...(RestDims) + 1> shape() const {
        return {FirstDim, RestDims...};
    }
};
