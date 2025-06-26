def list_comprehension_fn():
    # List comprehension to create a list of squares
    squares: list[int] = [x * x for x in range(10)]
    print(f"Squares: {squares}")

    # # List comprehension with a condition
    # even_squares = [x * x for x in range(10) if x % 2 == 0]
    # print(f"Even Squares: {even_squares}")
    #
    # # Nested list comprehension
    # matrix = [[j for j in range(3)] for i in range(3)]
    # print(f"Matrix: {matrix}")
    #
    # # Flattening a list of lists using list comprehension
    # flattened = [item for sublist in matrix for item in sublist]
    # print(f"Flattened: {flattened}")
    #
    # # Using list comprehension with functions
    # def square(x):
    #     return x * x
    #
    # squares_func = [square(x) for x in range(10)]
    # print(f"Squares using function: {squares_func}")
