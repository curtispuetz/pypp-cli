cmake_minimum_required(VERSION 4.0)

project(pyppDefaultProjectName LANGUAGES CXX)

# C++ standard settings
set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
# for clangd and tooling support (creates compile_commands.json in build/)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# Collect all .cpp source files from src/ directory recursively
file(GLOB_RECURSE SRC_FILES src/*.cpp)

# Define the executable with main.cpp and all src/*.cpp files
add_executable(pyppDefaultExeName
    main.cpp
    ${SRC_FILES}
)

# Add the src directory to the include path, scoped to this target
target_include_directories(pyppDefaultExeName
    PRIVATE
        ${CMAKE_SOURCE_DIR}/src
)

# Link any needed libraries here (empty for now)
# target_link_libraries(executable_name PRIVATE some_library)