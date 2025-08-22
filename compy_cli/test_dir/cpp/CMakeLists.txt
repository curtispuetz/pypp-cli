cmake_minimum_required(VERSION 4.0)
project(compy LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

file(GLOB_RECURSE SRC_FILES src/*.cpp)
file(GLOB_RECURSE COMPY_FILES compy/*.cpp)
file(GLOB_RECURSE LIB_FILES libs/*.cpp)

add_library(compy_common STATIC ${SRC_FILES} ${COMPY_FILES} ${LIB_FILES})
target_include_directories(compy_common PUBLIC ${CMAKE_SOURCE_DIR}/src ${CMAKE_SOURCE_DIR}/compy ${CMAKE_SOURCE_DIR}/libs)

add_executable(main main.cpp)
target_link_libraries(main PRIVATE compy_common)

add_executable(second_executable_example second_executable_example.cpp)
target_link_libraries(second_executable_example PRIVATE compy_common)
