def ternary_op_fn():
    print("TERNARY OP RESULTS:")
    a: int = 5
    b: int = 10
    max_value: int = a if a > b else b
    print(max_value)
