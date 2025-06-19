#pragma once

#include "exceptions/stdexcept.h"
#include <optional>
#include <ostream>
#include <vector>

struct PySlice {
  private:
    std::vector<int> _compute_slice_indices(int start, std::optional<int> stop,
                                            int step,
                                            int collection_length) const;

  public:
    int m_start;
    std::optional<int> m_stop;
    int m_step;

    explicit PySlice(int stop) : m_start(0), m_stop(stop), m_step(1) {}
    PySlice(int start, std::optional<int> stop, int step = 1)
        : m_start(start), m_stop(stop), m_step(step) {}
    std::vector<int> compute_slice_indices(int collection_length) const;
    void print(std::ostream &os) const;
    bool operator==(const PySlice &other) const;
    friend std::ostream &operator<<(std::ostream &os, const PySlice &pyslice);
};

namespace std {
// Hash function for usage as key in PyDict and PySet
template <> struct hash<PySlice> {
    size_t operator()(const PySlice &slice) const {
        std::size_t seed = 0;
        seed ^= std::hash<int>()(slice.m_start) + 0x9e3779b9 + (seed << 6) +
                (seed >> 2);
        if (slice.m_stop.has_value()) {
            seed ^= std::hash<int>()(*slice.m_stop) + 0x9e3779b9 + (seed << 6) +
                    (seed >> 2);
        } else {
            seed ^= std::hash<std::nullptr_t>()(nullptr) + 0x9e3779b9 +
                    (seed << 6) + (seed >> 2);
        }
        seed ^= std::hash<int>()(slice.m_step) + 0x9e3779b9 + (seed << 6) +
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