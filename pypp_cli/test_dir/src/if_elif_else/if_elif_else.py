def if_elif_else_fn(a: int, b: int) -> str:
    ret: str
    if a < b:
        ret = "less than"
    elif a == b:
        ret = "equal"
    else:
        ret = "greater than"
    return ret


def if_elif_elif_else_fn(a: int, b: int) -> str:
    ret: str
    if a < b:
        ret = "less than"
    elif a == b:
        ret = "equal"
    elif a > b:
        ret = "dunno"
    else:
        ret = "greater than"
    return ret
