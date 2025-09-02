def var_not_out_of_scope(condition: bool) -> int:
    m: int
    if condition:
        m = 42
    else:
        m = 100
    return 10 * m
