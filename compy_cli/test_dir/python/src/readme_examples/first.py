def my_function(a: list[int], b: list[int]) -> list[int]:
    ret: list[int] = [1, 2, 3]
    assert len(a) == len(b), "List lengths should be equal"
    for i in range(len(a)):
        ret.append(a[i] + b[i])
    return ret
