#include "index_calculator.h"

namespace pypp {
int calc_stop_index(std::optional<int> stop, int step, int collection_size) {
    int ret;
    if (step > 0) {
        if (!stop.has_value() || stop.value() > collection_size) {
            ret = collection_size;
        } else {
            ret = stop.value();
        }
    } else { // step < 0
        if (!stop.has_value()) {
            ret = -1;
        } else if (stop.value() > collection_size - 1) {
            ret = collection_size - 1;
        } else {
            ret = stop.value();
        }
    }
    return ret;
}

int calc_start_index(std::optional<int> start, int step, int collection_size) {
    // TODO later: this code is confusing! I am not sure if it is right for what
    // I want.
    //  But now I have tested it thoroughly so it seems like its probably
    //  working and I can leave it until a bug is found.
    int ret;
    if (step > 0) {
        if (!start.has_value()) {
            ret = 0;
        } else if (start.value() > collection_size) {
            ret = collection_size;
        } else {
            ret = start.value();
        }
    } else { // step < 0
        if (!start.has_value() || start.value() > collection_size - 1) {
            ret = collection_size - 1;
        } else {
            ret = start.value();
        }
    }
    return ret;
}
} // namespace pypp