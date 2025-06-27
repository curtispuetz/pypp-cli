type Matrix = list[list[int]]


def type_aliases_fn():
    print("TYPE ALIASES RESULTS:")
    # Using the type alias
    my_matrix: Matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"My matrix: {my_matrix}")
    # Using the type alias in a function (this wont work for now because Matrix needs
    # to go in the header file and not the cpp file.
    # TODO: test this ones the type alias is in the header file.


#     result: int = process_matrix(my_matrix)
#     print(f"first elem: {result}")
#
# def process_matrix(m: Matrix) -> int:
#     return m[0][0]
