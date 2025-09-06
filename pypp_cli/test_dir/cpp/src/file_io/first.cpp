#include "file_io/first.h"
#include "py_list.h"
#include "py_str.h"
#include "pypp_os.h"
#include "pypp_resources.h"
#include "pypp_shutil.h"
#include "pypp_text_io.h"
#include "pypp_util/print.h"

void file_io_fn() {
    pypp::print(pypp::PyStr("FILE IO RESULTS:"));
    pypp::PyStr test_dir = pypp::pypp_get_resources(pypp::PyStr("test_dir"));
    pypp::print(test_dir);
    pypp::PyStr text_file =
        pypp::os::path::join(test_dir, pypp::PyStr("text.txt"));
    pypp::print(text_file);
    if (!pypp::os::path::exists(test_dir)) {
        pypp::print(
            pypp::PyStr("test directory does not exist, creating it..."));
        pypp::os::makedirs(test_dir);
    } else {
        pypp::print(
            pypp::PyStr("test directory already exists, deleting it..."));
        pypp::shutil::rmtree(test_dir);
        pypp::print(pypp::PyStr("creating it again..."));
        pypp::os::makedirs(test_dir);
    }
    if (pypp::os::path::isdir(test_dir)) {
        pypp::print(pypp::PyStr("test_dir is a directory"));
    }
    if (pypp::os::path::isfile(test_dir)) {
        pypp::print(pypp::PyStr("test_dir is a file"));
    }
    {
        pypp::PyTextIO file(text_file, pypp::PyStr("w"));
        file.write(pypp::PyStr("Line 1\n"));
        file.write(pypp::PyStr("Line 2\n"));
        pypp::print(pypp::PyStr("finished writing to the file"));
    }
    {
        pypp::PyTextIO file(text_file, pypp::PyStr("a"));
        file.writelines(
            pypp::PyList({pypp::PyStr("Line 3\n"), pypp::PyStr("Line 4\n")}));
        pypp::print(pypp::PyStr("finished appending to the file"));
    }
    pypp::PyStr dir_name = pypp::os::path::dirname(text_file);
    pypp::PyStr base_name = pypp::os::path::basename(text_file);
    pypp::print(pypp::PyStr(std::format("dirname: {}", dir_name)));
    pypp::print(pypp::PyStr(std::format("basename: {}", base_name)));
    {
        pypp::PyTextIO file(text_file, pypp::PyStr("r"));
        pypp::PyStr content = file.read();
        pypp::print(pypp::PyStr(std::format(
            "Content of the file: {}",
            content.replace(pypp::PyStr("\n"), pypp::PyStr("\\n")))));
    }
    {
        pypp::PyTextIO file(text_file, pypp::PyStr("r"));
        pypp::PyStr line = file.readline();
        while (line != pypp::PyStr("")) {
            pypp::print(pypp::PyStr(std::format("Line: {}", line.strip())));
            line = file.readline();
        }
    }
    {
        pypp::PyTextIO file(text_file, pypp::PyStr("r"));
        pypp::PyList<pypp::PyStr> lines = file.readlines();
        pypp::PyList<pypp::PyStr> stripped_lines({});
        for (const auto &line : lines) {
            stripped_lines.append(line.strip());
        }
        pypp::print(pypp::PyStr(std::format("Lines: {}", stripped_lines)));
    }
}
