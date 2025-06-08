#pragma once

struct PySlice {
    int start;
    int stop;
    int step;

    PySlice(int start, int stop, int step = 1)
        : start(start), stop(stop), step(step) {}
};
