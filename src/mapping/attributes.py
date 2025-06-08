ATTRIBUTE_MAP: dict[str, str] = {
    # TODO: how can I make this only apply for lists!? Because right now
    #  any append attribute will be overwritten.
    "append": "push_back"
}


def lookup_cpp_attr(python_attr: str) -> str:
    if python_attr not in ATTRIBUTE_MAP:
        return python_attr
    return ATTRIBUTE_MAP[python_attr]
