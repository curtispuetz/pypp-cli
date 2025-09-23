cmake_minimum_required(VERSION 4.0)
set(CMAKE_CXX_COMPILER clang++)
set(CMAKE_C_COMPILER clang)
project(pypp LANGUAGES C CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

include(FetchContent)
FetchContent_Declare(
    glfw
    GIT_REPOSITORY https://github.com/glfw/glfw.git
    GIT_TAG 3.4
)
FetchContent_MakeAvailable(glfw)
include(FetchContent)
FetchContent_Declare(
    glad
    GIT_REPOSITORY https://github.com/Dav1dde/glad.git
    GIT_TAG v2.0.8
    GIT_PROGRESS TRUE
    SOURCE_SUBDIR cmake
)
FetchContent_MakeAvailable(glad)
glad_add_library(glad_gl_core_43 STATIC REPRODUCIBLE LOADER API gl:core=4.3)
# hello world!

set(SRC_FILES
other_src/first.cpp
src/args_test.cpp
src/augment_operations.cpp
src/constants.cpp
src/empty_return.cpp
src/first.cpp
src/fourth.cpp
src/lambdas.cpp
src/operations.cpp
src/pass_by_value.cpp
src/ref_vars.cpp
src/second.cpp
src/subscriptable_types.cpp
src/ternary_op.cpp
src/third.cpp
src/transpiler_config_test.cpp
src/triple_quote_strings.cpp
src/type_aliases.cpp
src/using_pass.cpp
src/built_in_functions/dict_fn.cpp
src/built_in_functions/list_fn.cpp
src/built_in_functions/number_conversions.cpp
src/built_in_functions/set_fn.cpp
src/dataclasses_test/first.cpp
src/dataclasses_test/nested_dependencies.cpp
src/dataclasses_test/with_methods.cpp
src/default_dict/create_with_defaults.cpp
src/default_dict/first.cpp
src/default_dict/methods.cpp
src/default_dict/operations.cpp
src/dicts/comprehensions.cpp
src/dicts/exceptions.cpp
src/dicts/first.cpp
src/dicts/looping.cpp
src/dicts/operations.cpp
src/exceptions/assert_.cpp
src/exceptions/custom_exceptions.cpp
src/exceptions/test_all.cpp
src/exceptions/throw_.cpp
src/file_io/first.cpp
src/file_io/shutil_exceptions.cpp
src/file_io/test_is_here.cpp
src/file_io/text_io_exceptions.cpp
src/fn_as_vars/first.cpp
src/if_elif_else/if_elif_else.cpp
src/imports_test/first.cpp
src/imports_test/second.cpp
src/inconsistent_behviour/editing_a_reference.cpp
src/inconsistent_behviour/reassigning_a_ref.cpp
src/interfaces/first.cpp
src/interfaces/with_dataclasses.cpp
src/lists/as_arg.cpp
src/lists/comprehensions.cpp
src/lists/declaration.cpp
src/lists/exceptions.cpp
src/lists/lists.cpp
src/lists/operations.cpp
src/lists/ownership.cpp
src/loops/enumerate_.cpp
src/loops/for_.cpp
src/loops/for_examples.cpp
src/loops/reversed_.cpp
src/loops/while_.cpp
src/loops/zip_.cpp
src/numbers_test/first.cpp
src/number_types/in_collections.cpp
src/number_types/number_types.cpp
src/printing/first.cpp
src/pypp_union/first.cpp
src/ranges/first.cpp
src/readme_examples/dataclasses.cpp
src/readme_examples/first.cpp
src/readme_examples/not_out_of_scope.cpp
src/readme_examples/out_of_scope.cpp
src/readme_examples/pass_by_value.cpp
src/readme_examples/return_by_reference.cpp
src/readme_examples/union.cpp
src/sets/comprehensions.cpp
src/sets/exceptions.cpp
src/sets/first.cpp
src/sets/of_tuples.cpp
src/sets/operations.cpp
src/slices/first.cpp
src/strings/exceptions.cpp
src/strings/first.cpp
src/strings/f_strings.cpp
src/strings/special_characters.cpp
src/tuples/exceptions.cpp
src/tuples/first.cpp
src/yields/first.cpp
src/stl/math_library/first.cpp
src/stl/os_library/first.cpp
src/stl/random_library/first.cpp
src/stl/time_library/first.cpp
src/custom_libs/bridge_lib_test_0/first.cpp
src/custom_libs/bridge_lib_test_1/first.cpp
src/custom_libs/pure_lib_test_0/first.cpp
src/benchmarking/perlin_noise/caller.cpp
src/benchmarking/perlin_noise/impl.cpp
)
file(GLOB_RECURSE pypp_FILES pypp/*.cpp)
file(GLOB_RECURSE LIB_FILES libs/*.cpp)

add_library(
    pypp_common STATIC
    ${SRC_FILES}
    ${pypp_FILES}
    ${LIB_FILES}
)
target_include_directories(
    pypp_common PUBLIC
    ${CMAKE_SOURCE_DIR}
    ${CMAKE_SOURCE_DIR}/pypp
    ${CMAKE_SOURCE_DIR}/libs
)
target_link_libraries(
    pypp_common PUBLIC
    glfw
    glad_gl_core_43
)

add_executable(glfw_test glfw_test.cpp)
target_link_libraries(glfw_test PRIVATE pypp_common)

add_executable(glfw_test_2 glfw_test_2.cpp)
target_link_libraries(glfw_test_2 PRIVATE pypp_common)

add_executable(main main.cpp)
target_link_libraries(main PRIVATE pypp_common)

add_executable(opengl_test opengl_test.cpp)
target_link_libraries(opengl_test PRIVATE pypp_common)

add_executable(second_executable_example second_executable_example.cpp)
target_link_libraries(second_executable_example PRIVATE pypp_common)
