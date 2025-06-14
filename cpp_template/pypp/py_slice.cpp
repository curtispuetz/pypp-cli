#include "py_slice.h"

std::vector<int> compute_slice_indices(int start, std::optional<int> stop,
                                       int step, int n) {
    std::vector<int> result;

    int stop_val = stop.value_or(n);

    if (start < 0)
        start += n;
    if (stop_val < 0)
        stop_val += n;

    if (start < 0)
        start = 0;
    if (stop_val > n)
        stop_val = n;

    if (step > 0 && start < stop_val) {
        for (int i = start; i < stop_val; i += step)
            result.push_back(i);
    } else if (step < 0 && start > stop_val) {
        for (int i = start; i > stop_val; i += step)
            result.push_back(i);
    }

    return result;
}
