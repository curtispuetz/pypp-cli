from pypp_python import time, auto
# TODO: change import to `from pypp_python.stl import time`.
# Add all other standard library imports as well.


def time_library_fn():
    print("TIME LIBRARY RESULTS (depends on time of execution):")
    a: auto = time.start()
    time.sleep(0.01)
    b: float = time.end(a)
    print(f"time.time() elapsed time: {b}")
    c: auto = time.perf_counter_start()
    time.sleep(0.01)
    d: float = time.perf_counter_end(c)
    print(f"performance time elapsed time: {d}")
