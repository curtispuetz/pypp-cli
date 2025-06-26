def f_strings_fn():
    print("F STRING RESULTS:")
    a: str = f"this {'is'} my {1}st test f string"
    print(a)
    my_set: set[int] = {1, 2}
    my_dict: dict[int, int] = {0: 1}
    b: str = (
        f"list: {[1, 2]}, tuple: {(1, 2)}, set: {my_set}, dict: {my_dict}, "
        f"slice: {slice(10)}, range: {range(1)}"
    )
    print(b)
