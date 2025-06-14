#include <array>
#include <iostream>

// --- Depth helper ---
template <size_t... Dims> struct DimHelper;

template <> struct DimHelper<> {
    static constexpr size_t value = 0;
};

template <size_t First, size_t... Rest> struct DimHelper<First, Rest...> {
    static constexpr size_t value = 1 + DimHelper<Rest...>::value;
};

// --- Forward declaration ---
template <typename T, size_t... Dims> class MultiArray;

// --- Base case: 1D array ---
template <typename T, size_t LastDim> class MultiArray<T, LastDim> {
  public:
    using Storage = std::array<T, LastDim>;
    Storage data;

    T &operator[](size_t idx) { return data[idx]; }
    const T &operator[](size_t idx) const { return data[idx]; }

    constexpr std::array<size_t, 1> shape() const { return {LastDim}; }

    // Example method: all()
    bool all() const {
        for (const auto &val : data) {
            if (!val)
                return false;
        }
        return true;
    }

    // Example method: any()
    bool any() const {
        for (const auto &val : data) {
            if (val)
                return true;
        }
        return false;
    }

    void print(std::ostream &os, int depth, int max_depth,
               bool dont_add_new_line) const {
        os << "[";
        for (size_t i = 0; i < LastDim; ++i) {
            os << data[i];
            if (i != LastDim - 1)
                os << ", ";
        }
        os << "]";
        if (!dont_add_new_line)
            os << std::string(max_depth - depth, '\n');
    }

    void print() const { print(std::cout, 0, 1, false); }
};

// --- Recursive case ---
template <typename T, size_t FirstDim, size_t... RestDims>
class MultiArray<T, FirstDim, RestDims...> {
  public:
    using SubArray = MultiArray<T, RestDims...>;
    using Storage = std::array<SubArray, FirstDim>;
    static constexpr int MaxDepth = DimHelper<FirstDim, RestDims...>::value;

    Storage data;

    SubArray &operator[](size_t idx) { return data[idx]; }
    const SubArray &operator[](size_t idx) const { return data[idx]; }

    constexpr std::array<size_t, sizeof...(RestDims) + 1> shape() const {
        return {FirstDim, RestDims...};
    }

    void print(std::ostream &os, int depth, int max_depth,
               bool dont_add_new_line) const {
        os << "[";
        for (size_t i = 0; i < FirstDim; ++i) {
            data[i].print(os, depth + 1, max_depth, i == FirstDim - 1);
        }
        os << "]";
        if (!dont_add_new_line) {
            if (depth > 0) {
                os << std::string(max_depth - depth, '\n');
            } else {
                os << "\n";
            }
        }
    }

    void print() const { print(std::cout, 0, MaxDepth, false); }
};
