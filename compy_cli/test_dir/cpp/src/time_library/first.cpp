#include "time_library/first.h"
#include "compy_time.h"
#include "compy_util/print.h"
#include "py_str.h"

void time_library_fn() {
    print(PyStr("TIME LIBRARY RESULTS (depends on time of execution):"));
    auto a = compy_time::start();
    compy_time::sleep(0.01);
    double b = compy_time::end(a);
    print(PyStr(std::format("time.time() elapsed time: {}", b)));
    auto c = compy_time::perf_counter_start();
    compy_time::sleep(0.01);
    double d = compy_time::perf_counter_end(c);
    print(PyStr(std::format("performance time elapsed time: {}", d)));
}
