#pragma once

#include "py_tuple.h"
#include <optional>
#include <stdexcept>

struct PySlice {
  public:
    PySlice(std::optional<int> start, std::optional<int> stop, int step);

    int stop_index(int collection_size) const;
    int start_index(int collection_size) const;
    PyTup<int, int, int> indices(int collection_size) const;
    int calc_slice_length(int collection_size) const;

    std::optional<int> start() const { return _start; }
    std::optional<int> stop() const { return _stop; }
    int step() const { return _step; }
    void print(std::ostream &os) const;
    bool operator==(const PySlice &other) const;
    friend std::ostream &operator<<(std::ostream &os, const PySlice &pyslice);

  private:
    std::optional<int> _start;
    std::optional<int> _stop;
    int _step;
};

namespace std {
// Hash function for usage as key in PyDict and PySet
template <> struct hash<PySlice> {
    size_t operator()(const PySlice &slice) const {
        std::size_t seed = 0;
        if (slice.start().has_value()) {
            seed ^= std::hash<int>()(*slice.start()) + 0x9e3779b9 +
                    (seed << 6) + (seed >> 2);
        } else {
            seed ^= std::hash<std::nullptr_t>()(nullptr) + 0x9e3779b9 +
                    (seed << 6) + (seed >> 2);
        }
        if (slice.stop().has_value()) {
            seed ^= std::hash<int>()(*slice.stop()) + 0x9e3779b9 + (seed << 6) +
                    (seed >> 2);
        } else {
            seed ^= std::hash<std::nullptr_t>()(nullptr) + 0x9e3779b9 +
                    (seed << 6) + (seed >> 2);
        }
        seed ^= std::hash<int>()(slice.step()) + 0x9e3779b9 + (seed << 6) +
                (seed >> 2);
        return seed;
    }
};
// Formatter for std::format
template <> struct formatter<PySlice> : formatter<string> {
    constexpr auto parse(format_parse_context &ctx) { return ctx.begin(); }

    template <typename FormatContext>
    auto format(const PySlice &pyslice, FormatContext &ctx) const {
        std::ostringstream oss;
        pyslice.print(oss);
        return std::format_to(ctx.out(), "{}", oss.str());
    }
};
} // namespace std