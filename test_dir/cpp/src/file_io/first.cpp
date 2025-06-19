#include "file_io\first.h"
#include "py_str.h"
#include "pypp_resources.h"
#include "pypp_text_io.h"
#include "pypp_util/print.h"

void file_io_fn() {
    PyStr text_file = pypp_get_resources(PyStr("test.txt"));
    print(text_file);
    {
        PyTextIO file(text_file, PyStr("w"));
        file.write(PyStr("Line 1\n"));
    }
}