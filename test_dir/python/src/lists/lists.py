def list_fn() -> int:
    my_list: list[int] = [1, 2, 3, 4, 5]
    my_list[0] = 10
    return my_list[0]
