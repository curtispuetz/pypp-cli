#include "src/stl/time_library/first.h"
#include "py_str.h"
#include "pypp_time.h"
#include "pypp_util/print.h"

namespace me {
void time_library_fn() {
    pypp::print(
        pypp::PyStr("TIME LIBRARY RESULTS (depends on time of execution):"));
    auto a = pypp::time::start();
    pypp::time::sleep(0.01);
    double b = pypp::time::end(a);
    pypp::print(pypp::PyStr(std::format("time.time() elapsed time: {}", b)));
    auto c = pypp::time::perf_counter_start();
    pypp::time::sleep(0.01);
    double d = pypp::time::perf_counter_end(c);
    pypp::print(
        pypp::PyStr(std::format("performance time elapsed time: {}", d)));
}

} // namespace me