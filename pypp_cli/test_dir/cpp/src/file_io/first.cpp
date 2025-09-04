#include "file_io/first.h"
#include "py_list.h"
#include "py_str.h"
#include "pypp_os.h"
#include "pypp_resources.h"
#include "pypp_shutil.h"
#include "pypp_text_io.h"
#include "pypp_util/print.h"

void file_io_fn() {
    print(PyStr("FILE IO RESULTS:"));
    PyStr test_dir = pypp_get_resources(PyStr("test_dir"));
    print(test_dir);
    PyStr text_file = os::path::join(test_dir, PyStr("text.txt"));
    print(text_file);
    if (!os::path::exists(test_dir)) {
        print(PyStr("test directory does not exist, creating it..."));
        os::makedirs(test_dir);
    } else {
        print(PyStr("test directory already exists, deleting it..."));
        shutil::rmtree(test_dir);
        print(PyStr("creating it again..."));
        os::makedirs(test_dir);
    }
    if (os::path::isdir(test_dir)) {
        print(PyStr("test_dir is a directory"));
    }
    if (os::path::isfile(test_dir)) {
        print(PyStr("test_dir is a file"));
    }
    {
        PyTextIO file(text_file, PyStr("w"));
        file.write(PyStr("Line 1\n"));
        file.write(PyStr("Line 2\n"));
        print(PyStr("finished writing to the file"));
    }
    {
        PyTextIO file(text_file, PyStr("a"));
        file.writelines(PyList({PyStr("Line 3\n"), PyStr("Line 4\n")}));
        print(PyStr("finished appending to the file"));
    }
    PyStr dir_name = os::path::dirname(text_file);
    PyStr base_name = os::path::basename(text_file);
    print(PyStr(std::format("dirname: {}", dir_name)));
    print(PyStr(std::format("basename: {}", base_name)));
    {
        PyTextIO file(text_file, PyStr("r"));
        PyStr content = file.read();
        print(PyStr(std::format("Content of the file: {}",
                                content.replace(PyStr("\n"), PyStr("\\n")))));
    }
    {
        PyTextIO file(text_file, PyStr("r"));
        PyStr line = file.readline();
        while (line != PyStr("")) {
            print(PyStr(std::format("Line: {}", line.strip())));
            line = file.readline();
        }
    }
    {
        PyTextIO file(text_file, PyStr("r"));
        PyList<PyStr> lines = file.readlines();
        PyList<PyStr> stripped_lines = PyList<PyStr>({});
        for (const auto &line : lines) {
            stripped_lines.append(line.strip());
        }
        print(PyStr(std::format("Lines: {}", stripped_lines)));
    }
}
