import os

dirname: str = os.path.dirname(__file__)
src_dir = os.path.join(dirname, "..", "..", "..", "Projects", "cpp_playground")
cml = "CMakeLists.txt"

# Config
parent_dir = os.path.join(src_dir, "app_benchmarking")
subproject_name = "enumerate"

if __name__ == "__main__":
    parent_cmake_lists = os.path.join(parent_dir, cml)
    subproject_dir_name = f"app_{subproject_name}"
    subproject_dir = os.path.join(parent_dir, subproject_dir_name)
    new_cmake_lists = os.path.join(subproject_dir, cml)
    new_main = os.path.join(subproject_dir, "main.cpp")

    os.mkdir(subproject_dir)
    # Write new cmake file
    with open(new_cmake_lists, "w") as file:
        file.writelines(
            [
                f"add_executable({subproject_name}_test main.cpp)\n",
                f"target_link_libraries({subproject_name}_test PRIVATE pypp_common)",
            ]
        )
    # add subproject to parent cmakefile
    with open(parent_cmake_lists, "a") as file:
        file.write(f"\nadd_subdirectory({subproject_dir_name})")
    # Add a main file with empty int main() function
    with open(new_main, "w") as file:
        file.writelines([
            "#include <pypp_util/main_error_handler.h>\n",
            '#include <cstdlib>  // Required for EXIT_FAILURE'
            "\n",
            "int main() {\n",
            "    try {\n",
            "        return 0;\n",
            "    } catch (...) {\n",
            "        handle_fatal_exception();\n",
            "        return EXIT_FAILURE;\n",
            "    }\n",
            "}\n"
        ])
