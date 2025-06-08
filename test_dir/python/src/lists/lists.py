def list_fn() -> int:
    my_list: list[int] = [1, 2, 3, 4, 5]
    my_list[0] = 10
    my_list.append(11)
    return my_list[-1]
