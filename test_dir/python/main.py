from src.first import return_something
from src.second import return_friend
from src.third import using_inline_string
from src.fourth import string_as_argument
from src.if_elif_else import if_elif_else_fn

if __name__ == "__main__":
    print(return_something(1, 9))
    print(return_friend())
    print(using_inline_string())
    print(string_as_argument("hello"))
    print(if_elif_else_fn(6, 6))
