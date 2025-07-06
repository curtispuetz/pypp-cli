#include "py_list.h"
#include "py_str.h"
#include "pypp_util/main_error_handler.h"
#include "pypp_util/print.h"
#include "src/dicts/comprehensions.h"
#include "src/dicts/exceptions.h"
#include "src/dicts/first.h"
#include "src/excpetions/assert_.h"
#include "src/excpetions/throw_.h"
#include "src/file_io/first.h"
#include "src/first.h"
#include "src/fourth.h"
#include "src/if_elif_else/if_elif_else.h"
#include "src/inconsistent_behviour/editing_a_reference.h"
#include "src/lists/as_arg.h"
#include "src/lists/comprehensions.h"
#include "src/lists/exceptions.h"
#include "src/lists/lists.h"
#include "src/loops/enumerate_.h"
#include "src/loops/for_.h"
#include "src/loops/reversed_.h"
#include "src/loops/while_.h"
#include "src/loops/zip_.h"
#include "src/math_library/first.h"
#include "src/numbers/first.h"
#include "src/printing/first.h"
#include "src/ranges/first.h"
#include "src/ref_vars.h"
#include "src/second.h"
#include "src/sets/comprehensions.h"
#include "src/sets/exceptions.h"
#include "src/sets/first.h"
#include "src/sets/of_tuples.h"
#include "src/slices/first.h"
#include "src/strings/escape_characters.h"
#include "src/strings/exceptions.h"
#include "src/strings/f_strings.h"
#include "src/strings/first.h"
#include "src/third.h"
#include "src/time_library/first.h"
#include "src/tuples/exceptions.h"
#include "src/tuples/first.h"
#include "src/type_aliases.h"
#include "src/yields/first.h"

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
        return 0;
    } catch (...) {
        handle_fatal_exception();
        return EXIT_FAILURE;
    }
}