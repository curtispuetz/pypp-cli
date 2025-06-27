from test_dir.python.pypp.custom_types import auto
from test_dir.python.pypp.stl.pypp_time import (
    pypp_time_sleep,
    pypp_time_start,
    pypp_time_end,
    pypp_time_perf_counter_start,
    pypp_time_perf_counter_end,
)


def time_library_fn():
    print("TIME LIBRARY RESULTS (depends on time of execution):")
    a: auto = pypp_time_start()
    pypp_time_sleep(0.01)
    b: float = pypp_time_end(a)
    print(f"time.time() elapsed time: {b}")
    c: auto = pypp_time_perf_counter_start()
    pypp_time_sleep(0.01)
    d: float = pypp_time_perf_counter_end(c)
    print(f"performance time elapsed time: {d}")
