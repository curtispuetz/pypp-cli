from test_dir.python.pypp.custom_types import auto
import test_dir.python.pypp.stl.pypp_time as pypp_time


def time_library_fn():
    print("TIME LIBRARY RESULTS (depends on time of execution):")
    a: auto = pypp_time.start()
    pypp_time.sleep(0.01)
    b: float = pypp_time.end(a)
    print(f"time.time() elapsed time: {b}")
    c: auto = pypp_time.perf_counter_start()
    pypp_time.sleep(0.01)
    d: float = pypp_time.perf_counter_end(c)
    print(f"performance time elapsed time: {d}")
