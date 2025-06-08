#include "py_slice.h"

std::vector<int> compute_slice_indices(int start, int stop, int step, int n) {
    std::vector<int> result;

    if (stop == NULL) stop = n;
    // Handle negative indexing
    if (start < 0) start += n;
    if (stop < 0) stop += n;

    // Clamp boundaries
    if (start < 0) start = 0;
    if (stop > n) stop = n;

    if (step > 0 && start < stop) {
        for (int i = start; i < stop; i += step)
            result.push_back(i);
    } else if (step < 0 && start > stop) {
        for (int i = start; i > stop; i += step)
            result.push_back(i);
    }

    return result;
}