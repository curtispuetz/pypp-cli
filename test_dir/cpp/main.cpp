#include "classes/first.h"
#include "classes/inheritance.h"
#include "constants.h"
#include "dataclasses_test/first.h"
#include "dataclasses_test/with_methods.h"
#include "default_dict/first.h"
#include "dicts/comprehensions.h"
#include "dicts/exceptions.h"
#include "dicts/first.h"
#include "excpetions/assert_.h"
#include "excpetions/throw_.h"
#include "file_io/first.h"
#include "first.h"
#include "fn_as_vars/first.h"
#include "fourth.h"
#include "if_elif_else/if_elif_else.h"
#include "inconsistent_behviour/editing_a_reference.h"
#include "interfaces/first.h"
#include "lists/as_arg.h"
#include "lists/comprehensions.h"
#include "lists/exceptions.h"
#include "lists/lists.h"
#include "loops/enumerate_.h"
#include "loops/for_.h"
#include "loops/reversed_.h"
#include "loops/while_.h"
#include "loops/zip_.h"
#include "math_library/first.h"
#include "numbers_test/first.h"
#include "operations.h"
#include "printing/first.h"
#include "py_list.h"
#include "py_str.h"
#include "pypp_union/first.h"
#include "pypp_util/main_error_handler.h"
#include "pypp_util/print.h"
#include "ranges/first.h"
#include "ref_vars.h"
#include "second.h"
#include "sets/comprehensions.h"
#include "sets/exceptions.h"
#include "sets/first.h"
#include "sets/of_tuples.h"
#include "slices/first.h"
#include "strings/escape_characters.h"
#include "strings/exceptions.h"
#include "strings/f_strings.h"
#include "strings/first.h"
#include "third.h"
#include "time_library/first.h"
#include "tuples/exceptions.h"
#include "tuples/first.h"
#include "type_aliases.h"
#include "yields/first.h"

int main() {
    try {
        print(return_something(1, 9));
        print(return_friend());
        print(using_inline_string());
        print(string_as_argument(PyStr("hello")));
        print(if_elif_else_fn(6, 6));
        number_ops();
        PyList<int> my_list = PyList({1, 2, 3, 4});
        list_as_arg(my_list);
        list_as_mutable_arg(my_list);
        print(my_list);
        PyList<PyStr> str_list = PyList({PyStr("ab"), PyStr("cd")});
        print(str_list);
        string_ops();
        set_fn();
        for_loop_fn();
        while_loop_fn();
        throw_fn();
        dict_exceptions_fn();
        list_exceptions_fn();
        set_exceptions_fn();
        string_exceptions_fn();
        tuple_exceptions_fn();
        string_esc_chars_fn();
        f_strings_fn();
        ranges_fn();
        slices_fn();
        editing_a_reference_fn();
        enumerate_fn();
        printing_fn();
        zip_fn();
        reversed_fn();
        file_io_fn();
        set_comprehension_fn();
        dict_comprehension_fn();
        list_comprehension_fn();
        assert_fn();
        type_aliases_fn();
        yield_fn();
        math_library_fn();
        time_library_fn();
        tuples_fn();
        set_of_tuples_fn();
        ref_vars_fn();
        dict_fn();
        list_fn();
        dataclass_fn();
        dataclass_with_methods_fn();
        classes_fn();
        class_inheritance_fn();
        interfaces_fn();
        operations_fn();
        fn_as_vars_fn();
        default_dict_fn();
        pypp_union_fn();
        constant_fn();
        return 0;
    } catch (...) {
        handle_fatal_exception();
        return EXIT_FAILURE;
    }
}