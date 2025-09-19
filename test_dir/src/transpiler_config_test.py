from pypp_python import configclass, dataclass, Valu


def a_function_i_like():
    print("I like functions!")


def a_function_i_like_extra():
    print("I like functions!")


@configclass
class _ConfigClassA:
    a: int = 10


@configclass
class _ConfigClassB:
    b: int = 20


@dataclass
class AnnAssignCustomType:
    x: Valu(str)


@dataclass
class AnnAssignOtherType:
    x: Valu(str)


def transpiler_config_test_fn():
    print("TRANSPILER CONFIG TEST:")
    crazy_name: str = "crazy"
    print(crazy_name)
    a_function_i_like()
    a: AnnAssignCustomType = AnnAssignCustomType("hello")
    print(a.x)
    print(_ConfigClassA.a)
