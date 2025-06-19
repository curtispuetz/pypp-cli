def string_esc_chars_fn():
    a: str = "\n"
    b: str = "abcd\n"
    c: str = "\t"
    d: str = "abcd\t"
    e: str = "\r"
    f: str = "abcd\r"
    g: str = "\b"
    h: str = "abcd\b"
    i: str = "\f"
    j: str = "abcd\f"
    k: str = "\\"
    l1: str = "abcd\\"
    print(a + b + c + d + e + f + g + h + i + j + k + l1)
    m: str = "abcd\\\\"
    print(m)
