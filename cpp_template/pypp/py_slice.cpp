#include "py_slice.h"

std::vector<int> PySlice::_compute_slice_indices(int start,
                                                 std::optional<int> stop,
                                                 int step,
                                                 int collection_length) const {
    if (step == 0) {
        throw PyppValueError("slice step cannot be zero");
    }
    std::vector<int> result;

    int stop_val = stop.value_or(collection_length);

    if (start < 0)
        start += collection_length;
    if (stop_val < 0)
        stop_val += collection_length;

    if (start < 0)
        start = 0;
    if (stop_val > collection_length)
        stop_val = collection_length;

    if (step > 0 && start < stop_val) {
        for (int i = start; i < stop_val; i += step)
            result.push_back(i);
    } else if (step < 0 && start > stop_val) {
        for (int i = start; i > stop_val; i += step)
            result.push_back(i);
    }

    return result;
}

std::vector<int> PySlice::compute_slice_indices(int collection_length) const {
    return _compute_slice_indices(m_start, m_stop, m_step, collection_length);
}

std::ostream &operator<<(std::ostream &os, const PySlice &pyslice) {
    os << "slice(" << pyslice.m_start << ", ";
    if (pyslice.m_stop.has_value()) {
        os << pyslice.m_stop.value();
    } else {
        os << "None";
    }
    return os << ", " << pyslice.m_step << ")";
}