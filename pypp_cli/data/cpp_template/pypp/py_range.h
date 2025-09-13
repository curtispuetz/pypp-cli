#pragma once

#include <exceptions/stdexcept.h>
#include <format>
#include <ostream>
#include <sstream>

namespace pypp {
struct PyRange {
  private:
    // The iterator class for PyRange.
    // It holds the current value in the sequence and the step.
    struct iterator {
        int m_current;
        const int m_step;

        // Dereference operator: returns the current value.
        int operator*() const { return m_current; }

        // Pre-increment operator: moves to the next value in the range.
        iterator &operator++() {
            m_current += m_step;
            return *this;
        }

        // Inequality operator: checks if the loop should continue.
        // This is the core logic for the range-based for loop.
        // It compares the current iterator's value against the 'end' iterator's
        // value.
        bool operator!=(const iterator &other) const {
            // If the step is positive, we continue as long as the current value
            // is less than the stop value.
            if (m_step > 0) {
                return m_current < other.m_current;
            }
            // If the step is negative, we continue as long as the current value
            // is greater than the stop value.
            else {
                return m_current > other.m_current;
            }
        }
    };

  public:
    const int m_start;
    const int m_stop;
    const int m_step;
    /**
     * @brief Constructor for a range with a start of 0 and a step of 1.
     * @example PyRange(10) -> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
     */
    explicit PyRange(int stop) : m_start(0), m_stop(stop), m_step(1) {}

    /**
     * @brief Constructor for a range with a specified start and stop.
     * @param start The starting value of the range (inclusive).
     * @param stop The ending value of the range (exclusive).
     * @param step The increment between values (defaults to 1).
     * @example PyRange(2, 10) -> 2, 3, 4, 5, 6, 7, 8, 9
     * @example PyRange(10, 2, -1) -> 10, 9, 8, 7, 6, 5, 4, 3
     */
    PyRange(int start, int stop, int step = 1)
        : m_start(start), m_stop(stop), m_step(step) {
        if (step == 0) {
            throw ValueError("range() arg 3 must not be zero");
        }
        // For a valid range, if step is positive, start should be less than
        // stop. If step is negative, start should be greater than stop. If
        // these conditions aren't met, the range is empty. The loop condition
        // will handle this correctly by not executing any iterations.
    }

    // Returns an iterator to the beginning of the range.
    iterator begin() const { return iterator{m_start, m_step}; }

    // Returns an iterator to the end of the range.
    // The 'end' iterator's value is the 'stop' value.
    iterator end() const { return iterator{m_stop, m_step}; }

    void print(std::ostream &os) const {
        os << "range(" << m_start << ", " << m_stop;
        if (m_step != 1) {
            os << ", " << m_step;
        }
        os << ")";
    }
    bool operator==(const PyRange &other) const {
        return m_start == other.m_start && m_stop == other.m_stop &&
               m_step == other.m_step;
    }
    friend std::ostream &operator<<(std::ostream &os, const PyRange &pyrange);
};

inline std::ostream &operator<<(std::ostream &os, const PyRange &pyrange) {
    pyrange.print(os);
    return os;
}

} // namespace pypp

namespace std {
// Hash function for usage as a key in PyDict and PySet
template <> struct hash<pypp::PyRange> {
    std::size_t operator()(const pypp::PyRange &p) const noexcept {
        std::size_t seed = 0;
        seed ^= std::hash<int>()(p.m_start) + 0x9e3779b9 + (seed << 6) +
                (seed >> 2);
        seed ^=
            std::hash<int>()(p.m_stop) + 0x9e3779b9 + (seed << 6) + (seed >> 2);
        seed ^=
            std::hash<int>()(p.m_step) + 0x9e3779b9 + (seed << 6) + (seed >> 2);
        return seed;
    }
};
// Formatter for std::format
template <> struct formatter<pypp::PyRange> : formatter<string> {
    constexpr auto parse(format_parse_context &ctx) { return ctx.begin(); }

    template <typename FormatContext>
    auto format(const pypp::PyRange &pyrange, FormatContext &ctx) const {
        std::ostringstream oss;
        pyrange.print(oss);
        return std::format_to(ctx.out(), "{}", oss.str());
    }
};
} // namespace std