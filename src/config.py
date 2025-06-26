import os

dirname: str = os.path.dirname(__file__)

# TODO: add a auto type just like the C++ auto type where you can use
#  it whenever you would be able to use it in C++. Like when
#  you can calling something and assigning it to a variable, the function
#  has a known type so you can always use auto.

C_TARGET_DIR: str = os.path.join(dirname, "../test_dir")
C_CPP_DIR: str = os.path.join(C_TARGET_DIR, "cpp")
C_CPP_BUILD_DIR: str = os.path.join(C_CPP_DIR, "build")
C_CPP_BUILD_RELEASE_DIR: str = os.path.join(C_CPP_BUILD_DIR, "Release")
C_CPP_MAIN_FILE: str = os.path.join(C_CPP_DIR, "main.cpp")
C_CPP_SRC_DIR: str = os.path.join(C_CPP_DIR, "src")
C_PYTHON_DIR: str = os.path.join(C_TARGET_DIR, "python")
C_PYTHON_MAIN_FILE: str = os.path.join(C_PYTHON_DIR, "main.py")
C_PYTHON_SRC_DIR: str = os.path.join(C_PYTHON_DIR, "src")

C_CPP_TEMPLATE_DIR: str = os.path.join(dirname, "../cpp_template")
