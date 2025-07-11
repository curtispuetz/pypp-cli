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
    # Show the nuance of how if you define a type alias at a non-module level and
    # without starting with an underscore, the type alias is actually extracted to the
    # header file in the transpiled C++. If the name starts with an underscore this is
    # not the case.
    type L = list[int]
    a: L = [1, 2, 3]
    print(a)


def process_matrix(m: Matrix) -> int:
    return m[0][0]
