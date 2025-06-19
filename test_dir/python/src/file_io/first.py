from test_dir.python.pypp.resources import pypp_get_resources


def file_io_fn():
    text_file: str = pypp_get_resources("test.txt")
    print(text_file)
    with open(text_file, "w") as file:
        file.write("Line 1\n")
    # TODO: keep testing the rest of the options. Also test os things
