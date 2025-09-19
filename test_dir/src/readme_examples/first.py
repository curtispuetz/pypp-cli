def list_add(a: list[int], b: list[int], mult_factor: int) -> list[int]:
    assert len(a) == len(b), "List lengths should be equal"
    ret: list[int] = []
    for i in range(len(a)):
        ret.append(mult_factor * (a[i] + b[i]))
    return ret
