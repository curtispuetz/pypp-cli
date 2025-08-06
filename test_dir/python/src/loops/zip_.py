from pypp_python.ownership import mov
from pypp_python.tuple_get import tg


def zip_fn():
    print("ZIP RESULTS:")
    # over two lists
    a: list[int] = []
    for x, z in zip([1, 2], [3, 4]):
        a.append(mov(x))
        a.append(mov(z))
    print(a)
    # over multiple different types. list, set, string, and dict items
    b: dict[float, int] = {1.1: 4, 2.2: 5}
    for x, z, y, w in zip([1, 2], {"a", "b"}, "ab", b.items()):
        # Note: The sets and dicts in C++ order is not guaranteed, so you could see
        # different strings
        print(f"{x}, {z}, {y}, {tg(w, 0)}, {tg(w, 0)}")
