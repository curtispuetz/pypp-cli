from pypp_python.ownership import Valu


def string_as_argument(input_str: Valu(str)) -> str:
    if input_str < "abc":
        return input_str
    return "abc"
