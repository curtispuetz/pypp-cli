#pragma once

#include "exceptions/stdexcept.h"
#include <optional>
#include <ostream>
#include <vector>

struct PySlice {
  private:
    int start;
    std::optional<int> stop;
    int step;

    std::vector<int> _compute_slice_indices(int start, std::optional<int> stop,
                                            int step,
                                            int collection_length) const;

  public:
    explicit PySlice(int a_stop) : start(0), stop(a_stop), step(1) {}
    PySlice(int a_start, std::optional<int> a_stop, int a_step = 1)
        : start(a_start), stop(a_stop), step(a_step) {}
    std::vector<int> compute_slice_indices(int collection_length) const;
    friend std::ostream &operator<<(std::ostream &os, const PySlice &pyslice);
};
