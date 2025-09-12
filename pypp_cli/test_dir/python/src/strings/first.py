from pypp_python import mov


def string_ops():
    print("STRING RESULTS:")
    # TODO later: there are a number of little string methods that I don't have tested
    #  below or implemented in PyStr
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
    print("invalid slice: ")
    # print(s[-6:-13421423:1345])
    # concatenation
    s_concat: str = "Hello " + "World"
    print(s_concat)
    print("Hello" + " " + "World" + "!")
    print("A" + "B")
    # repetition
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
    # replace
    print("abcdab".replace("ab", "xy"))
    print("abcdab".replace("ab", "xy", 1))
    # strip
    print(s.strip())
    print(s.lstrip())
    print(s.rstrip())
    # lexographical comparisons
    print(str("a" == "a"))
    print(str("a" > "a"))
    print(str("a" >= "a"))
    print(str("a" < "a"))
    print(str("a" <= "a"))
    print(str("a" != "a"))
    # aug assignments
    print(s)
    s += "n"
    s += ""
    print(s)
    s *= 5
    print(s)
    s *= -5
    print(s)
    # split
    l1: list[str] = "0,1,2".split(",")
    print(l1)
    l2: list[str] = "0 1 2".split()
    print(l2)
    # join
    print(" ".join(["1", "2", "3"]))
    s_joined: str = ", ".join(["a", "b", "c", "d"])
    print(s_joined)
    # initialize empty
    a: str = ""
    print(a)
    # iterate over a string
    list_of_chars: list[str] = []
    for c in "abcdefg":
        ch: str = c
        list_of_chars.append(mov(ch))
    print(list_of_chars)
    m: str = "abc"
    if "a" in m:
        print(f"a in {m}")
    if "d" not in m:
        print(f"d not in {m}")
    print(max(m))
    print(min(m))
    # raw string
    raw_s: str = r"this \n is a raw string with a \t tab and a \\ backslash"
    print(raw_s)
