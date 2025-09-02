from compy_python import mov


def set_comprehension_fn():
    print("SET COMPREHENSION RESULTS:")
    # Set comprehension to create a set of squares
    squares: set[int] = {x * x for x in range(4)}
    print(f"Squares: {squares}")
    # Testing with simple value and mov
    a: set[int] = {mov(i) for i in range(4)}
    print(a)
