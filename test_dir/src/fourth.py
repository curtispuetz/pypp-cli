from pypp_python import Val


def string_as_argument(input_str: Val[str]) -> str:
    if input_str < "abc":
        return input_str
    return "abc"
