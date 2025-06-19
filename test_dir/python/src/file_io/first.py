from test_dir.python.pypp.resources import pypp_get_resources


def file_io_fn():
    text_file: str = pypp_get_resources("test.txt")
    print(text_file)
    # TODO: handle escape characters like \n in strings. I think to solve this whenever
    #  I put something inside a PyStr() then I need to escape everything.
    with open(text_file, "w") as file:
        file.write("Line 1")
    # TODO: keep testing the rest of the options. Also test os things