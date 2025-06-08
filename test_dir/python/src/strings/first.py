def string_ops():
    # declaration
    s: str = "  abd  "
    # printing
    print(s)
    # getting length
    print(str(len(s)))
    # indexing
    print(s[2])
    # slicing/substring
    print(s[2:4])
    print(s[:4])
    print(s[3:])
    print(s[2:5:2])
    print(s[2::2])
    print(s[:])
    # concatenation
    s_concat: str = "Hello " + "World"
    print(s_concat)
    print("Hello" + " " + "World" + "!")
    print("A" + "B")
    print("AB" * 5)
    # Upper
    print("ab".upper())
    # Lower
    print("AB".lower())
    # Find
    print(str("abcdefg".find("b")))
    # Index
    print(str("abcbc".index("bc")))
    # rindex
    print(str("abab".rindex("ab")))
    # count
    print(str("ababab".count("ab")))
    # startswith
    print(str("abab".startswith("ab")))
    # endswith
    print(str("abab".endswith("ab")))
