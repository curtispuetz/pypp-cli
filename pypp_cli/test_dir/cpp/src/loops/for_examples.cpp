#include "loops/for_examples.h"
#include "py_enumerate.h"
#include "py_reversed.h"
#include "py_zip.h"
#include "pypp_util/print.h"

namespace me {
void pseudo_fn(pypp::PyList<int> &integers,
               pypp::PyList<pypp::PyStr> &strings) {
    for (const auto &integer : integers) {
        pypp::print(integer);
    }
    for (int i = 0; i < integers.len(); i += 1) {
        pypp::print(i);
    }
    for (int i = integers.len(); i < 5; i += -2) {
        pypp::print(i);
    }
    for (const auto &[i, val] : pypp::PyEnumerate(integers)) {
        pypp::print(i, val);
    }
    for (const auto &[integer, string] : pypp::PyZip(integers, strings)) {
        pypp::print(integer, string);
    }
    for (const auto &integer : pypp::PyReversed(integers)) {
        pypp::print(integer);
    }
    for (const auto &c : pypp::PyStr("abcdefg")) {
        pypp::print(c);
    }
}

} // namespace me