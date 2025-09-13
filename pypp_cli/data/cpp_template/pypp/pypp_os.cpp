#include "pypp_os.h"

#include "exceptions/filesystem.h"

namespace pypp {
namespace os {

void makedirs(const PyStr &p) {
    fs::path path = fs::path(p.str());
    if (fs::is_directory(path))
        throw FileExistsError(PyStr("os.makedirs(dir) dir already exists: ") +
                              p);
    try {
        if (!fs::create_directories(path))
            throw OSError(PyStr("os.makedirs(dir) dir not created: ") + p);
    } catch (const fs::filesystem_error &e) {
        if (e.code() == std::errc::permission_denied)
            throw PermissionError(PyStr(e.what()));
        throw OSError(PyStr(e.what()));
    }
}

void remove(const PyStr &p) {
    fs::path path = fs::path(p.str());
    if (fs::is_directory(path))
        throw OSError(PyStr("os.remove(path) path is a directory: ") + p);
    if (!fs::exists(path))
        throw FileNotFoundError(PyStr("No such file or directory: ") + p);
    try {
        if (!fs::remove(path))
            throw OSError(PyStr("File not removed: ") + p);
    } catch (const fs::filesystem_error &e) {
        if (e.code() == std::errc::permission_denied)
            throw PermissionError(PyStr(e.what()));
        throw OSError(PyStr(e.what()));
    }
}

void mkdir(const PyStr &p) {
    fs::path path = fs::path(p.str());
    if (fs::is_directory(path))
        throw FileExistsError(PyStr("os.mkdir(dir) dir already exists: ") + p);
    try {
        if (!fs::create_directory(path))
            throw OSError(PyStr("os.mkdir(dir) dir not created: ") + p);
    } catch (const fs::filesystem_error &e) {
        if (e.code() == std::errc::no_such_file_or_directory)
            throw FileNotFoundError(PyStr(e.what()));
        if (e.code() == std::errc::permission_denied)
            throw PermissionError(PyStr(e.what()));
        throw OSError(PyStr(e.what()));
    }
}

void rmdir(const PyStr &p) {
    try {
        fs::path path_obj(p.str());
        if (!fs::is_directory(path_obj))
            throw FileNotFoundError(
                PyStr("os.rmdir(dir) dir does not exist: " + p.str()));
        if (!fs::remove(path_obj))
            throw OSError(PyStr("os.rmdir(dir) dir is not empty: " + p.str()));
    } catch (const fs::filesystem_error &e) {
        if (e.code() == std::errc::permission_denied)
            throw PermissionError(PyStr(e.what()));
        throw OSError(PyStr(e.what()));
    }
}

void rename(const PyStr &src, const PyStr &dst) {
    if (fs::exists(fs::path(dst.str())))
        throw FileExistsError(
            PyStr("os.rename(src, dst) dst already exists: ") + dst);
    try {
        fs::rename(fs::path(src.str()), fs::path(dst.str()));
    } catch (const fs::filesystem_error &e) {
        if (e.code() == std::errc::no_such_file_or_directory)
            throw FileNotFoundError(PyStr(e.what()));
        if (e.code() == std::errc::permission_denied)
            throw PermissionError(PyStr(e.what()));
        throw OSError(PyStr(e.what()));
    }
}

PyList<PyStr> listdir(const PyStr &p) {
    PyList<PyStr> entries;
    try {
        fs::path path_obj(p.str());
        if (!fs::exists(path_obj))
            throw FileNotFoundError(PyStr("No such directory: " + p.str()));
        if (!fs::is_directory(path_obj))
            throw NotADirectoryError(PyStr("Not a directory: " + p.str()));
        for (const auto &entry : fs::directory_iterator(path_obj)) {
            entries.append(PyStr(entry.path().filename().string()));
        }
    } catch (const fs::filesystem_error &e) {
        if (e.code() == std::errc::permission_denied)
            throw PermissionError(PyStr(e.what()));
        throw OSError(PyStr(e.what()));
    }
    return entries;
}

namespace path {

bool exists(const PyStr &p) { return fs::exists(fs::path(p.str())); }

bool isdir(const PyStr &p) { return fs::is_directory(fs::path(p.str())); }

bool isfile(const PyStr &p) { return fs::is_regular_file(fs::path(p.str())); }

PyStr dirname(const PyStr &p) {
    return PyStr(fs::path(p.str()).parent_path().string());
}

PyStr basename(const PyStr &p) {
    return PyStr(fs::path(p.str()).filename().string());
}

PyTup<PyStr, PyStr> split(const PyStr &p) {
    fs::path path_obj(p.str());
    return PyTup(PyStr(path_obj.parent_path().string()),
                 PyStr(path_obj.filename().string()));
}

PyStr abspath(const PyStr &p) {
    return PyStr(fs::absolute(fs::path(p.str())).string());
}

} // namespace path
} // namespace os
} // namespace pypp
