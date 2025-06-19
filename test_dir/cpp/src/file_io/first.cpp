#include "file_io\first.h"

void file_io_fn() {
    PyStr text_file = pypp_get_resources(PyStr("test.txt"));
    text_file.print();
    {
        PyTextIO file(text_file, PyStr("w"));
        file.write(PyStr("Line 1"));
    }
}