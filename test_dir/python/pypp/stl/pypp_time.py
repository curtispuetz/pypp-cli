import time


def pypp_time_start() -> float:
    return time.time()


def pypp_time_end(start_time: float) -> float:
    return time.time() - start_time


def pypp_time_sleep(seconds: float) -> None:
    time.sleep(seconds)


def pypp_time_perf_counter_start() -> float:
    return time.perf_counter()


def pypp_time_perf_counter_end(start_time: float) -> float:
    return time.perf_counter() - start_time
