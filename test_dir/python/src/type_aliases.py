type Matrix = list[list[int]]
type _PrivateType = tuple[int, list[str], float]


def type_aliases_fn():
    print("TYPE ALIASES RESULTS:")
    # Using the type alias
    my_matrix: Matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"My matrix: {my_matrix}")
    # Using the type alias in a function
    result: int = process_matrix(my_matrix)
    print(f"first elem: {result}")
    # Using the private type alias
    private_data: _PrivateType = (42, ["example", "data"], 3.14)
    print(f"Private data: {private_data}")


def process_matrix(m: Matrix) -> int:
    return m[0][0]
