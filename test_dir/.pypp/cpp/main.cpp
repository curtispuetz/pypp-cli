#include "cstdlib"
#include "exceptions/exception.h"
#include "py_list.h"
#include "py_str.h"
#include "pypp_util/main_error_handler.h"
#include "pypp_util/print.h"
#include "src/args_test.h"
#include "src/augment_operations.h"
#include "src/benchmarking.h"
#include "src/built_in_functions/dict_fn.h"
#include "src/built_in_functions/list_fn.h"
#include "src/built_in_functions/number_conversions.h"
#include "src/built_in_functions/set_fn.h"
#include "src/constants.h"
#include "src/custom_libs/bridge_lib_test_0/first.h"
#include "src/custom_libs/bridge_lib_test_1/first.h"
#include "src/custom_libs/pure_lib_test_0/first.h"
#include "src/dataclasses_test/first.h"
#include "src/dataclasses_test/nested_dependencies.h"
#include "src/dataclasses_test/with_methods.h"
#include "src/default_dict/create_with_defaults.h"
#include "src/default_dict/first.h"
#include "src/default_dict/methods.h"
#include "src/default_dict/operations.h"
#include "src/dicts/comprehensions.h"
#include "src/dicts/exceptions.h"
#include "src/dicts/first.h"
#include "src/dicts/looping.h"
#include "src/dicts/operations.h"
#include "src/empty_return.h"
#include "src/exceptions/assert_.h"
#include "src/exceptions/custom_exceptions.h"
#include "src/exceptions/test_all.h"
#include "src/exceptions/throw_.h"
#include "src/file_io/first.h"
#include "src/file_io/shutil_exceptions.h"
#include "src/file_io/test_is_here.h"
#include "src/first.h"
#include "src/fn_as_vars/first.h"
#include "src/fourth.h"
#include "src/if_elif_else/if_elif_else.h"
#include "src/imports_test/first.h"
#include "src/imports_test/second.h"
#include "src/inconsistent_behviour/editing_a_reference.h"
#include "src/inconsistent_behviour/reassigning_a_ref.h"
#include "src/interfaces/first.h"
#include "src/interfaces/with_dataclasses.h"
#include "src/lambdas.h"
#include "src/lists/as_arg.h"
#include "src/lists/comprehensions.h"
#include "src/lists/declaration.h"
#include "src/lists/exceptions.h"
#include "src/lists/lists.h"
#include "src/lists/operations.h"
#include "src/lists/ownership.h"
#include "src/loops/enumerate_.h"
#include "src/loops/for_.h"
#include "src/loops/reversed_.h"
#include "src/loops/while_.h"
#include "src/loops/zip_.h"
#include "src/number_types/in_collections.h"
#include "src/number_types/number_types.h"
#include "src/numbers_test/first.h"
#include "src/operations.h"
#include "src/pass_by_value.h"
#include "src/printing/first.h"
#include "src/pypp_union/first.h"
#include "src/ranges/first.h"
#include "src/ref_vars.h"
#include "src/second.h"
#include "src/sets/comprehensions.h"
#include "src/sets/exceptions.h"
#include "src/sets/first.h"
#include "src/sets/of_tuples.h"
#include "src/sets/operations.h"
#include "src/slices/first.h"
#include "src/stl/math_library/first.h"
#include "src/stl/random_library/first.h"
#include "src/stl/time_library/first.h"
#include "src/strings/exceptions.h"
#include "src/strings/f_strings.h"
#include "src/strings/first.h"
#include "src/strings/special_characters.h"
#include "src/subscriptable_types.h"
#include "src/ternary_op.h"
#include "src/third.h"
#include "src/transpiler_config_test.h"
#include "src/triple_quote_strings.h"
#include "src/tuples/exceptions.h"
#include "src/tuples/first.h"
#include "src/type_aliases.h"
#include "src/using_pass.h"
#include "src/yields/first.h"
#include <utility>

static int _private_fn() { return 1; }

using _int_alias = int;
const int _A_CONST = 2;
struct __PseudoPyppName_AConfigClass {
    int x = 0;
    int y = 1;
};
inline __PseudoPyppName_AConfigClass _AConfigClass;

class _MyCustom : public pypp::Exception {
  public:
    explicit _MyCustom(const pypp::PyStr &msg)
        : pypp::Exception(pypp::PyStr("_MyCustom: ") + msg) {}
};

class _MyCInterface {
  public:
    virtual void a() = 0;
    virtual ~_MyCInterface() {}
};

struct MyDataClassInMain {
    pypp::PyList<int> my_list;
    MyDataClassInMain(pypp::PyList<int> a_my_list)
        : my_list(std::move(a_my_list)) {}
    pypp::PyList<int> calc_something() { return my_list * 4; }
};

int main() {
    try {
        pypp::print(_A_CONST);
        pypp::print(_AConfigClass.x);
        pypp::print(
            MyDataClassInMain(pypp::PyList({1, 2, 3})).calc_something());
        pypp::print(_private_fn());
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
        me::shutil_exceptions_fn();
        pypp::print(me::A, me::B, me::C, me::D, me::E, me::a, me::b);
        me::dict_looping_fn();
        me::pure_lib_test_0_fn();
        me::transpiler_config_test_fn();
        me::perlin_noise_fn();
        return 0;
    } catch (...) {
        pypp::handle_fatal_exception();
        return EXIT_FAILURE;
    }
}