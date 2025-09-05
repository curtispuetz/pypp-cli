cmake_minimum_required(VERSION 4.0)
project(pypp LANGUAGES CXX)

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

file(GLOB_RECURSE SRC_FILES src/*.cpp)
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
    ${CMAKE_SOURCE_DIR}/src
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

add_executable(second_executable_example second_executable_example.cpp)
target_link_libraries(second_executable_example PRIVATE pypp_common)
