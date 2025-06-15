def set_fn():
    # declaration
    a: set[int] = {1, 2, 3}
    print(a)
    # adding
    a.add(4)
    print(a)
    # discarding
    a.discard(4)
    print(a)
    # removing
    a.discard(3)
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
    # equality
    print(str({1, 2} == {1, 2}))
    print(str({1, 2} == {1, 2, 3}))
    # unequality
    print(str({1, 2} != {1, 2, 3}))
    print(str({1, 2} != {1, 2}))
    # clear
    a.clear()
    print(a)
    # list of sets
    list_of_sets: list[set[int]] = [{1, 2}, {3, 4}]
    print(list_of_sets)
    # initialize empty
    c: set[int] = set()
    print(c)
