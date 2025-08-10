cmake_minimum_required(VERSION 4.0)
project(pypp LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

file(GLOB_RECURSE SRC_FILES src/*.cpp)
file(GLOB_RECURSE PYPP_FILES pypp/*.cpp)
file(GLOB_RECURSE LIB_FILES libs/*.cpp)

add_library(pypp_common STATIC ${SRC_FILES} ${PYPP_FILES} ${LIB_FILES})
target_include_directories(pypp_common PUBLIC ${CMAKE_SOURCE_DIR}/src ${CMAKE_SOURCE_DIR}/pypp ${CMAKE_SOURCE_DIR}/libs)

add_executable(main main.cpp)
target_link_libraries(main PRIVATE pypp_common)

add_executable(second_executable_example second_executable_example.cpp)
target_link_libraries(second_executable_example PRIVATE pypp_common)
