import os

dirname: str = os.path.dirname(__file__)
src_dir = os.path.join(dirname, "..", "..", "..", "Projects", "cpp_playground")
cml = "CMakeLists.txt"

# Config
parent_dir = os.path.join(src_dir, "app_random_tests")
subproject_name_suffix = "printing"  # starts with app
use_subproject_name_suffix_as_executable_name_prefix = True
executable_name_prefix = "dict_benchmarking"  # if above is True, this doesn't matter
if use_subproject_name_suffix_as_executable_name_prefix:
    executable_name_prefix = subproject_name_suffix


if __name__ == "__main__":
    parent_cmake_lists = os.path.join(parent_dir, cml)
    subproject_dir_name = f"app_{subproject_name_suffix}"
    subproject_dir = os.path.join(parent_dir, subproject_dir_name)
    new_cmake_lists = os.path.join(subproject_dir, cml)
    new_main = os.path.join(subproject_dir, "main.cpp")

    os.mkdir(subproject_dir)
    # Write new cmake file
    with open(new_cmake_lists, "w") as file:
        file.writelines(
            [
                f"add_executable({executable_name_prefix}_test main.cpp)\n",
                f"target_link_libraries({executable_name_prefix}_test PRIVATE pypp_common)",
            ]
        )
    # add subproject to parent cmakefile
    with open(parent_cmake_lists, "a") as file:
        file.write(f"\nadd_subdirectory({subproject_dir_name})")
    # Add a main file with empty int main() function
    with open(new_main, "w") as file:
        file.writelines(
            [
                "#include <pypp_util/main_error_handler.h>\n",
                "#include <cstdlib>  // Required for EXIT_FAILURE\n",
                "\n",
                "\n",
                "int main() {\n",
                "    try {\n",
                "        return 0;\n",
                "    } catch (...) {\n",
                "        handle_fatal_exception();\n",
                "        return EXIT_FAILURE;\n",
                "    }\n",
                "}\n",
            ]
        )
