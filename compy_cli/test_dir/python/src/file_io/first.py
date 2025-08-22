from compy_python.resources import compy_get_resources
import os
import shutil


def file_io_fn():
    print("FILE IO RESULTS:")
    # compy_get_resources
    test_dir: str = compy_get_resources("test_dir")
    print(test_dir)
    # os.path.join
    text_file: str = os.path.join(test_dir, "text.txt")
    print(text_file)
    # os.path.exists, os.makedirs, and os.removedirs
    if not os.path.exists(test_dir):
        print("test directory does not exist, creating it...")
        os.makedirs(test_dir)
    else:
        print("test directory already exists, deleting it...")
        shutil.rmtree(test_dir)
        print("creating it again...")
        os.makedirs(test_dir)
    # os.path.isdir and os.path.isfile
    if os.path.isdir(test_dir):
        print("test_dir is a directory")
    if os.path.isfile(test_dir):
        print("test_dir is a file")
    # create and write a text file
    with open(text_file, "w") as file:
        file.write("Line 1\n")
        file.write("Line 2\n")
        print("finished writing to the file")
    # writelines with append mode
    with open(text_file, "a") as file:
        file.writelines(["Line 3\n", "Line 4\n"])
        print("finished appending to the file")
    # dirname and basename
    dir_name: str = os.path.dirname(text_file)
    base_name: str = os.path.basename(text_file)
    print(f"dirname: {dir_name}")
    print(f"basename: {base_name}")
    # read the text file completely
    with open(text_file, "r") as file:
        content: str = file.read()
        print(f"Content of the file: {content.replace('\n', '\\n')}")
    # read the text file line by line
    with open(text_file, "r") as file:
        line: str = file.readline()
        while line != "":
            print(f"Line: {line.strip()}")
            line = file.readline()
    # readlines
    with open(text_file, "r") as file:
        lines: list[str] = file.readlines()
        stripped_lines: list[str] = []
        for line in lines:
            stripped_lines.append(line.strip())
        print(f"Lines: {stripped_lines}")
    # TODO later: more testing
