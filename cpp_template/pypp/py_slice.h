#pragma once

#include "exceptions/stdexcept.h"
#include <optional>
#include <ostream>
#include <vector>

struct PySlice {
  private:
    int m_start;
    std::optional<int> m_stop;
    int m_step;

    std::vector<int> _compute_slice_indices(int start, std::optional<int> stop,
                                            int step,
                                            int collection_length) const;

  public:
    explicit PySlice(int stop) : m_start(0), m_stop(stop), m_step(1) {}
    PySlice(int start, std::optional<int> stop, int step = 1)
        : m_start(start), m_stop(stop), m_step(step) {}
    std::vector<int> compute_slice_indices(int collection_length) const;
    friend std::ostream &operator<<(std::ostream &os, const PySlice &pyslice);
};
