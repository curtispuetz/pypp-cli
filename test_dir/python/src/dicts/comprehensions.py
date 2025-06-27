def dict_comprehension_fn():
    print("DICT COMPREHENSION RESULTS:")
    # Dict comprehension to create a dictionary of squares
    squares: dict[int, int] = {x: x * x for x in range(4)}
    print(f"Squares: {squares}")
