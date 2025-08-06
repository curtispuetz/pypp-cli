import time


def start() -> float:
    return time.time()


def end(start_time: float) -> float:
    return time.time() - start_time


def sleep(seconds: float) -> None:
    time.sleep(seconds)


def perf_counter_start() -> float:
    return time.perf_counter()


def perf_counter_end(start_time: float) -> float:
    return time.perf_counter() - start_time
