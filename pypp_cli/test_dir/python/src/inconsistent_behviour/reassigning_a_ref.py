from pypp_python import Ref


# Rule of thumb:
# - do not reassign a reference variable.


# Implication:
# If you have a global state (say a list), and somewhere in your huge codebase
# you have a functions whos argument is a reference to that list, and you want to
# completely reassign it


def modifying_a_ref(l: list[int]):
    l = [-1, 3]


def reassigning_a_ref_fn():
    print("REASSIGNING A REF RESULTS:")
    a: list[int] = [1, 2, 3]
    b: Ref(list[int]) = a
    b.append(4)
    print(a)
    print(b)
    # Now, what if we reassign b to a new list?
    b = [10, 20, 30]  # This is not modifying the original list a!
    print(f"{a} (should be [10, 20, 30] in C++)")  # should print [1, 2, 3, 4]
    print(b)  # should print [10, 20, 30]

    # example 2
    c: list[int] = [1, 2, 3]
    modifying_a_ref(c)
    print(f"{c} (should be [-1, 3] in C++)")  # should print [1, 2, 3]


# Solution to this problem
