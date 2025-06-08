def list_fn() -> str:
    my_list: list[int] = [1, 2, 3, 4, 5]
    my_list[0] = 10
    my_list.append(11)
    return str(my_list[-1])
