from collections import defaultdict
from dataclasses import dataclass

from test_dir.python.pypp.printing import print_address


def _dict_factory() -> dict[int, int]:
    return {1: 2, 3: 4}


@dataclass
class _CustomType:
    val: int


def default_dict_fn():
    print("DEFAULT DICT RESULTS:")
    # creation without specifying a default factory function
    a: defaultdict[int, int] = defaultdict(int)
    b: int = a[0]
    print(b)
    print(a)
    c: defaultdict[int, float] = defaultdict(float)
    d: float = c[0]
    print(d)
    print(c)
    e: defaultdict[int, bool] = defaultdict(bool)
    f: bool = e[0]
    print(f)
    print(e)
    g: defaultdict[int, str] = defaultdict(str)
    h: str = g[0]
    print(h)
    print(g)
    i: defaultdict[int, list[int]] = defaultdict(list[int])
    j: list[int] = i[0]
    print(j)
    print(i)
    k: defaultdict[int, dict[int, int]] = defaultdict(dict[int, int])
    l: dict[int, int] = k[0]
    print(l)
    print(k)
    m: defaultdict[int, set[int]] = defaultdict(set[int])
    n: set[int] = m[0]
    print(n)
    print(m)
    # creation with a default factory function
    o: defaultdict[int, int] = defaultdict(lambda: 42)
    p: int = o[0]
    print(p)
    print(o)
    q: defaultdict[int, float] = defaultdict(lambda: 3.14)
    r: float = q[0]
    print(r)
    print(q)
    s: defaultdict[int, bool] = defaultdict(lambda: True)
    t: bool = s[0]
    print(t)
    print(s)
    u: defaultdict[int, str] = defaultdict(lambda: "default")
    v: str = u[0]
    print(v)
    print(u)
    w: defaultdict[int, list[int]] = defaultdict(lambda: [1, 2, 3])
    x: list[int] = w[0]
    print(x)
    print(w)
    y: defaultdict[int, dict[int, int]] = defaultdict(_dict_factory)
    z: dict[int, int] = y[0]
    print(z)
    print(y)
    aa: defaultdict[int, set[int]] = defaultdict(lambda: {1, 2, 3})
    ab: set[int] = aa[0]
    print(ab)
    print(aa)
    # modification
    w[9].append(99)
    print(w)
    # with a custom type
    ac: defaultdict[int, _CustomType] = defaultdict(lambda: _CustomType(42))
    ad: _CustomType = ac[0]
    print(ad.val)
    print_address(ad)
