from pypp_python import Ref, Valu, auto, dataclass, defaultdict


def _dict_factory() -> dict[int, int]:
    return {1: 2, 3: 4}


def _default_dict_as_arg(a: Valu(defaultdict[int, int])):
    print(a[0])


@dataclass
class _CustomType:
    val: int


def default_dict_fn():
    print("DEFAULT DICT RESULTS:")
    # creation without specifying a default factory function
    a: auto = defaultdict[int, int](int)
    b: int = a[0]
    print(b)
    print(a)
    c: auto = defaultdict[int, float](float)
    d: float = c[0]
    print(d)
    print(c)
    e: auto = defaultdict[int, bool](bool)
    f: bool = e[0]
    print(f)
    print(e)
    g: auto = defaultdict[int, str](str)
    h: str = g[0]
    print(h)
    print(g)
    i: auto = defaultdict[int, list[int]](list[int])
    j: list[int] = i[0]
    print(j)
    print(i)
    k: auto = defaultdict[int, dict[int, int]](dict[int, int])
    l: dict[int, int] = k[0]
    print(l)
    print(k)
    m: auto = defaultdict[int, set[int]](set[int])
    n: set[int] = m[0]
    print(n)
    print(m)
    # creation with a default factory function
    o: auto = defaultdict[int, int](lambda: 42)
    p: int = o[0]
    print(p)
    print(o)
    q: auto = defaultdict[int, float](lambda: 3.14)
    r: float = q[0]
    print(r)
    print(q)
    s: auto = defaultdict[int, bool](lambda: True)
    t: bool = s[0]
    print(t)
    print(s)
    u: auto = defaultdict[int, str](lambda: "default")
    v: str = u[0]
    print(v)
    print(u)
    w: auto = defaultdict[int, list[int]](lambda: [1, 2, 3])
    x: list[int] = w[0]
    print(x)
    print(w)
    y: auto = defaultdict[int, dict[int, int]](_dict_factory)
    z: dict[int, int] = y[0]
    print(z)
    print(y)
    aa: auto = defaultdict[int, set[int]](lambda: {1, 2, 3})
    ab: set[int] = aa[0]
    print(ab)
    print(aa)
    # modification
    w[9].append(99)
    print(w)
    # with a custom type
    ac: auto = defaultdict[int, _CustomType](lambda: _CustomType(42))
    ad: _CustomType = ac[0]
    print(ad.val)
    print(Ref[ad])
    # as an argument
    _default_dict_as_arg(defaultdict[int, int](int))
