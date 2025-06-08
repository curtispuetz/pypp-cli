def list_fn():
    # Declaration
    a: list[int] = [1, 2, 3, 4, 5]
    print(a)
    # Assigning element
    a[0] = 10
    print(a)
    # Append
    a.append(11)
    print(a)
    # Accessing - indices
    print(str(a[-1]))
    # Showing modification behaviour
    b: int = a[-1]
    print(str(b))
    b = 20
    print(str(b))
    print(a)
    # Len
    print(str(len(a)))
    # reverse
    a.reverse()
    print(a)