def square(x: int) -> int:
    return x * x


def list_comprehension_fn():
    print("LIST COMPREHENSION RESULTS:")
    # List comprehension to create a list of squares
    squares: list[int] = [x * x for x in range(10)]
    print(f"Squares: {squares}")
    # Using list comprehension with functions
    squares_func: list[int] = [square(x) for x in range(10)]
    print(f"Squares using function: {squares_func}")
