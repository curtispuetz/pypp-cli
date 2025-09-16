def string_esc_chars_fn():
    print("STRING ESC CHARS RESULTS:")
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
    n: str = "with escaping quotes: '' \"hello\" and backslash \\ and newline \n"
    print(n)
    n0: str = "with escaping quotes: '' \"hello\""
    print(n0)
    n1: str = 'with escaping quotes: \' "hello"'
    print(n1)
    # with f-strings
    o: str = f"with escaping {1} quotes: '' \"hello\" and backslash \\ and newline \n"
    print(o)
    p: str = f'with quotes {2} again with \' a single quoted f-string "hello"'
    print(p)
    # escaping special characters
    q: str = "escaping special chars: \\n, \\t, \\r, \\b, \\f, \\\\, '\""
    print(q)
