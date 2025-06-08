def using_inline_string() -> str:
    if "a" > "b":  # NOTE: don't do this. The C++ wont convert these to std::string
        return "10"
    return "5"
