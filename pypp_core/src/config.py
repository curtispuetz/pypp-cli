import os

dirname: str = os.path.dirname(__file__)

# TODO later: add a auto type just like the C++ auto type where you can use
#  it whenever you would be able to use it in C++. Like when
#  you can calling something and assigning it to a variable, the function
#  has a known type so you can always use auto.

C_TARGET_DIR: str = os.path.join(dirname, "../test_dir")
C_CPP_DIR: str = os.path.join(C_TARGET_DIR, "cpp")
C_CPP_BUILD_DIR: str = os.path.join(C_CPP_DIR, "build")
C_CPP_BUILD_RELEASE_DIR: str = os.path.join(C_CPP_BUILD_DIR, "Release")
C_CPP_SRC_DIR: str = os.path.join(C_CPP_DIR, "src")
C_PYTHON_DIR: str = os.path.join(C_TARGET_DIR, "python")
C_PYTHON_SRC_DIR: str = os.path.join(C_PYTHON_DIR, "src")

C_CPP_TEMPLATE_DIR: str = os.path.join(dirname, "../cpp_template")


class PyppDirs:
    def __init__(self, target_dir: str):
        self.target_dir = target_dir
        self.cpp_dir: str = os.path.join(C_TARGET_DIR, "cpp")
        self.cpp_build_dir: str = os.path.join(C_CPP_DIR, "build")
        self.cpp_build_release_dir: str = os.path.join(C_CPP_BUILD_DIR, "Release")
        self.cpp_src_dir: str = os.path.join(C_CPP_DIR, "src")
        self.python_dir: str = os.path.join(C_TARGET_DIR, "python")
        self.python_src_dir: str = os.path.join(C_PYTHON_DIR, "src")
        self.cpp_template_dir: str = os.path.join(dirname, "../cpp_template")
