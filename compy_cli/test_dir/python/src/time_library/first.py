from compy_python import compy_time, auto


def time_library_fn():
    print("TIME LIBRARY RESULTS (depends on time of execution):")
    a: auto = compy_time.start()
    compy_time.sleep(0.01)
    b: float = compy_time.end(a)
    print(f"time.time() elapsed time: {b}")
    c: auto = compy_time.perf_counter_start()
    compy_time.sleep(0.01)
    d: float = compy_time.perf_counter_end(c)
    print(f"performance time elapsed time: {d}")
