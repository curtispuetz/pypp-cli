from pypp_python import Callable


def lambdas_fn():
    print("LAMBDA RESULTS:")
    a: Callable[[int], int] = lambda x: x // 2
    print(a(5))
