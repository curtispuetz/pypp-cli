def set_comprehension_fn():
    print("SET COMPREHENSION RESULTS:")
    # Set comprehension to create a set of squares
    squares: set[int] = {x * x for x in range(4)}
    print(f"Squares: {squares}")