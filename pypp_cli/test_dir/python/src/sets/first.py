from pypp_python import mov, Valu


def _inline_set(s: Valu(set[float])):
    print(s)


def set_fn():
    print("SET RESULTS:")
    # declaration
    a: set[int] = {1, 2, 3}
    print(a)
    # initialize empty
    c: set[int] = set[int]()
    print(c)
    # adding
    a.add(4)
    print(a)
    # adding with mov
    add_val: int = 4
    a.add(mov(add_val))
    # discarding
    a.discard(4)
    print(a)
    # removing
    a.remove(3)
    print(a)
    # contains
    print(str(1 in a))
    # union
    b: set[int] = {1, 5}
    print(a.union(b))
    # intersection
    print(a.intersection(b))
    # difference
    print(a.difference(b))
    # symmetric difference
    print(a.symmetric_difference(b))
    # update
    a.update({6, 7})
    print(a)
    a.update([9, 10])
    print(a)
    # intersection update
    a.intersection_update(b)
    print(a)
    # symmetric difference update
    a.symmetric_difference_update(b)
    print(a)
    # difference update
    a.difference_update({6})
    print(a)
    # len
    print(str(len(b)))
    # issubset
    print(str({1, 2}.issubset({1, 2, 3})))
    print(str({1, 4}.issubset({1, 2, 3})))
    # issuperset
    print(str({1, 2, 3}.issuperset({1, 2})))
    print(str({1, 4, 3}.issuperset({1, 2})))
    # isdisjoint
    print({1, 2}.isdisjoint({3, 4}))
    print({1, 2}.isdisjoint({2, 3}))
    # equality
    print(str({1, 2} == {1, 2}))
    print(str({1, 2} == {1, 2, 3}))
    # unequality
    print(str({1, 2} != {1, 2, 3}))
    print(str({1, 2} != {1, 2}))
    # clear
    a.clear()
    print(a)
    # pop
    print(b.pop())
    print(b)
    # copy
    d: set[int] = {1, 2}
    e: set[int] = d.copy()
    d.add(3)
    print(f"original: {d}, copied set: {e}")
    # list of sets
    list_of_sets: list[set[int]] = [{1, 2}, {3, 4}]
    print(list_of_sets)
    # inline passing
    _inline_set({1.2, 4.4})
