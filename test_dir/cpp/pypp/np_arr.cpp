#include "np_arr_util.h"
namespace pypp_np {
PyList<size_t> convert_int_shape_to_size_t(const PyList<int> &shape) {
    PyList<size_t> shape_size_t;
    for (const auto &dim : shape) {
        if (dim < 0) {
            throw PyppValueError("negative dimensions are not allowed");
        }
        shape_size_t.append(static_cast<size_t>(dim));
    }
    return shape_size_t;
}
} // namespace pypp_np