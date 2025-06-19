#include "pypp_text_io.h"
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>

void PyTextIO::check_file_open() const {
    if (!file_stream.is_open()) {
        throw std::runtime_error("File not open: " + filename_.str());
    }
}

void PyTextIO::check_file_open_for_writing() const {
    if (!file_stream.is_open()) {
        throw std::runtime_error("File not open for writing: " +
                                 filename_.str());
    }
}

void PyTextIO::open_file(const PyStr &filename, const PyStr &mode) {
    std::ios_base::openmode cpp_mode = std::ios_base::in;

    if (mode.str() == "r") {
        cpp_mode = std::ios_base::in;
    } else if (mode.str() == "w") {
        cpp_mode = std::ios_base::out | std::ios_base::trunc;
    } else if (mode.str() == "a") {
        cpp_mode = std::ios_base::out | std::ios_base::app;
    } else if (mode.str() == "r+") {
        cpp_mode = std::ios_base::in | std::ios_base::out;
    } else if (mode.str() == "w+") {
        cpp_mode =
            std::ios_base::in | std::ios_base::out | std::ios_base::trunc;
    } else if (mode.str() == "a+") {
        cpp_mode = std::ios_base::in | std::ios_base::out | std::ios_base::app;
    } else {
        throw std::runtime_error("Unsupported file mode: " + mode.str());
    }

    file_stream.open(filename.str(), cpp_mode);
    if (!file_stream.is_open()) {
        throw std::runtime_error("Could not open file: " + filename.str() +
                                 " with mode " + mode.str());
    }
}

PyTextIO::PyTextIO(const PyStr &filename, const PyStr &mode)
    : filename_(filename), mode_(mode) {
    open_file(filename_, mode_);
}

PyTextIO::~PyTextIO() {
    if (file_stream.is_open()) {
        file_stream.close();
    }
}

PyStr PyTextIO::read() {
    check_file_open();
    file_stream.clear();
    file_stream.seekg(0);

    std::stringstream buffer;
    buffer << file_stream.rdbuf();
    return PyStr(buffer.str());
}

PyStr PyTextIO::readline() {
    check_file_open();
    std::string line;
    if (std::getline(file_stream, line)) {
        return PyStr(line + "\n");
    }
    return PyStr("");
}

PyList<PyStr> PyTextIO::readlines() {
    check_file_open();
    file_stream.clear();
    file_stream.seekg(0);

    std::vector<PyStr> lines;
    std::string line;
    while (std::getline(file_stream, line)) {
        lines.push_back(PyStr(line + "\n"));
    }
    return PyList(lines);
}

void PyTextIO::write(const PyStr &content) {
    check_file_open_for_writing();
    file_stream << content.str();
    if (file_stream.fail()) {
        throw std::runtime_error("Error writing to file: " + filename_.str());
    }
}

void PyTextIO::writelines(const PyList<PyStr> &lines) {
    check_file_open_for_writing();
    for (const PyStr &line : lines) {
        file_stream << line.str();
    }
    if (file_stream.fail()) {
        throw std::runtime_error("Error writing lines to file: " +
                                 filename_.str());
    }
}

bool PyTextIO::good() const { return file_stream.good(); }

bool PyTextIO::eof() const { return file_stream.eof(); }

bool PyTextIO::fail() const { return file_stream.fail(); }
