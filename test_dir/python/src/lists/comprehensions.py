def list_comprehension_fn():
    # List comprehension to create a list of squares
    squares: list[int] = [x * x for x in range(10)]
    print(f"Squares: {squares}")
    # # Using list comprehension with functions
    # def square(x):
    #     return x * x
    #
    # squares_func = [square(x) for x in range(10)]
    # print(f"Squares using function: {squares_func}")
