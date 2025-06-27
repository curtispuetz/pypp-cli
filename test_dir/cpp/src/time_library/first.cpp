#include "time_library\first.h"
#include "py_str.h"
#include "pypp_time.h"
#include "pypp_util/print.h"

void time_library_fn() {
    print(PyStr("TIME LIBRARY RESULTS (depends on time of execution):"));
    auto a = pypp_time::start();
    pypp_time::sleep(0.01);
    double b = pypp_time::end(a);
    print(PyStr(std::format("time.time() elapsed time: {}", b)));
    auto c = pypp_time::perf_counter_start();
    pypp_time::sleep(0.01);
    double d = pypp_time::perf_counter_end(c);
    print(PyStr(std::format("performance time elapsed time: {}", d)));
}