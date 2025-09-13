#include "args_test.h"
#include "augment_operations.h"
#include "built_in_functions/dict_fn.h"
#include "built_in_functions/list_fn.h"
#include "built_in_functions/number_conversions.h"
#include "built_in_functions/set_fn.h"
#include "constants.h"
#include "cstdlib"
#include "custom_libs/bridge_lib_test_0/first.h"
#include "custom_libs/bridge_lib_test_1/first.h"
#include "dataclasses_test/first.h"
#include "dataclasses_test/nested_dependencies.h"
#include "dataclasses_test/with_methods.h"
#include "default_dict/create_with_defaults.h"
#include "default_dict/first.h"
#include "default_dict/methods.h"
#include "default_dict/operations.h"
#include "dicts/comprehensions.h"
#include "dicts/exceptions.h"
#include "dicts/first.h"
#include "dicts/operations.h"
#include "empty_return.h"
#include "exceptions/assert_.h"
#include "exceptions/custom_exceptions.h"
#include "exceptions/test_all.h"
#include "exceptions/throw_.h"
#include "file_io/first.h"
#include "file_io/test_is_here.h"
#include "first.h"
#include "fn_as_vars/first.h"
#include "fourth.h"
#include "if_elif_else/if_elif_else.h"
#include "imports_test/first.h"
#include "imports_test/second.h"
#include "inconsistent_behviour/editing_a_reference.h"
#include "inconsistent_behviour/reassigning_a_ref.h"
#include "interfaces/first.h"
#include "interfaces/with_dataclasses.h"
#include "lambdas.h"
#include "lists/as_arg.h"
#include "lists/comprehensions.h"
#include "lists/declaration.h"
#include "lists/exceptions.h"
#include "lists/lists.h"
#include "lists/operations.h"
#include "lists/ownership.h"
#include "loops/enumerate_.h"
#include "loops/for_.h"
#include "loops/reversed_.h"
#include "loops/while_.h"
#include "loops/zip_.h"
#include "math_library/first.h"
#include "number_types/in_collections.h"
#include "number_types/number_types.h"
#include "numbers_test/first.h"
#include "operations.h"
#include "pass_by_value.h"
#include "printing/first.h"
#include "py_list.h"
#include "py_str.h"
#include "pypp_union/first.h"
#include "pypp_util/main_error_handler.h"
#include "pypp_util/print.h"
#include "random_library/first.h"
#include "ranges/first.h"
#include "ref_vars.h"
#include "second.h"
#include "sets/comprehensions.h"
#include "sets/exceptions.h"
#include "sets/first.h"
#include "sets/of_tuples.h"
#include "sets/operations.h"
#include "slices/first.h"
#include "strings/exceptions.h"
#include "strings/f_strings.h"
#include "strings/first.h"
#include "strings/special_characters.h"
#include "subscriptable_types.h"
#include "ternary_op.h"
#include "third.h"
#include "time_library/first.h"
#include "triple_quote_strings.h"
#include "tuples/exceptions.h"
#include "tuples/first.h"
#include "type_aliases.h"
#include "using_pass.h"
#include "yields/first.h"

int main() {
    try {
        pypp::print(me::return_something(1, 9));
        pypp::print(me::return_friend());
        pypp::print(me::using_inline_string());
        pypp::print(me::string_as_argument(pypp::PyStr("hello")));
        pypp::print(me::if_elif_else_fn(6, 6));
        me::number_ops();
        pypp::PyList<int> my_list({1, 2, 3, 4});
        me::list_as_arg(my_list);
        me::list_as_mutable_arg(my_list);
        pypp::print(my_list);
        pypp::PyList<pypp::PyStr> str_list(
            {pypp::PyStr("ab"), pypp::PyStr("cd")});
        pypp::print(str_list);
        me::string_ops();
        me::set_fn();
        me::for_loop_fn();
        me::while_loop_fn();
        me::throw_fn();
        me::dict_exceptions_fn();
        me::list_exceptions_fn();
        me::set_exceptions_fn();
        me::string_exceptions_fn();
        me::tuple_exceptions_fn();
        me::string_esc_chars_fn();
        me::f_strings_fn();
        me::ranges_fn();
        me::slices_fn();
        me::editing_a_reference_fn();
        me::enumerate_fn();
        me::printing_fn();
        me::zip_fn();
        me::reversed_fn();
        me::file_io_fn();
        me::set_comprehension_fn();
        me::dict_comprehension_fn();
        me::list_comprehension_fn();
        me::assert_fn();
        me::type_aliases_fn();
        me::yield_fn();
        me::math_library_fn();
        me::tuples_fn();
        me::set_of_tuples_fn();
        me::ref_vars_fn();
        me::dict_fn();
        me::dataclass_fn();
        me::dataclass_with_methods_fn();
        me::interfaces_fn();
        me::operations_fn();
        me::fn_as_vars_fn();
        me::pypp_union_fn();
        me::constant_fn();
        me::imports_test_fn();
        me::imports_test_fn2();
        me::number_types_fn();
        me::time_library_fn();
        me::default_dict_fn();
        me::random_fn();
        me::custom_exception_fn();
        me::args_test_fn();
        me::subscriptable_types_fn();
        me::lambdas_fn();
        me::bridge_lib_test_0_fn();
        me::bridge_lib_test_1_fn();
        me::list_ownership_tests_fn();
        me::list_fn();
        me::dataclass_nested_dependencies_fn();
        me::triple_quote_strings_fn();
        me::number_types_in_collections_fn();
        me::test_is_here_fn();
        me::ternary_op_fn();
        me::list_declaration_fn();
        me::list_operations_fn();
        me::built_in_list_fn();
        me::built_in_set_fn();
        me::built_in_dict_fn();
        me::set_operations_fn();
        me::dict_operations_fn();
        me::default_dict_operations_fn();
        me::default_dict_methods_fn();
        me::default_dict_create_with_defaults();
        me::pass_by_value_test_fn();
        me::reassigning_a_ref_fn();
        me::pass_fn();
        me::interface_with_dataclasses_fn();
        me::number_conversions_fn();
        me::augment_operations_fn();
        me::empty_return_fn();
        me::test_all_exceptions_fn();
        return 0;
    } catch (...) {
        pypp::handle_fatal_exception();
        return EXIT_FAILURE;
    }
}