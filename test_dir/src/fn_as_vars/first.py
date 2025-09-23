from pypp_python import Val, dataclass, Callable


def _test_fn(a: int, b: int) -> str:
    return f"{a} {b}"


def _test_fn2(fn: Callable[[], float]):
    print(fn())


def _test_fn3() -> float:
    return 2.71


def _test_fn4(a: int):
    print(a)


def _test_fn5():
    print("test fn5 called")


def _test_fn6(fn: Val[Callable[[int, int], str]]):
    print(fn(1, 2))


@dataclass
class TestClass:
    def t(self, fn: Callable[[], None]):
        fn()


@dataclass
class TestDataClass:
    a: int

    def t(self, fn: Callable[[], None]):
        fn()


def fn_as_vars_fn():
    print("FN_AS_VARS RESULTS:")
    # assign function to variable
    fn_var: Callable[[int, int], str] = _test_fn
    print(fn_var(1, 2))
    # passing function as argument
    a: Callable[[], float] = _test_fn3
    _test_fn2(a)
    # function that doesn't return anything
    b: Callable[[int], None] = _test_fn4
    b(5)
    # function that doesn't return anything or take arguments
    c: Callable[[], None] = _test_fn5
    c()
    # passing a function as a method argument
    d: TestClass = TestClass()
    d.t(c)
    # passing a function as dataclass method argument
    e: TestDataClass = TestDataClass(1)
    e.t(c)
    # creating a lambda function
    f: Callable[[int, int], str] = lambda x, y: f"Lambda {x, y}"
    print(f(3, 4))
    # passing a lambda as argument
    _test_fn6(lambda x, y: f"Lambda {x, y}")
    # lambda without any arguments
    g: Callable[[], str] = lambda: "Lambda without args"
    print(g())
