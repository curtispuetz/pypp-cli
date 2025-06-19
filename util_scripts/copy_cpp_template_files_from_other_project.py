import os
import shutil

dirname: str = os.path.dirname(__file__)

if __name__ == "__main__":
    src_dir = os.path.join(dirname, "..", "..", "..", "Projects", "cpp_playground")
    target_dir = os.path.join(dirname, "..", "cpp_template")
    shutil.rmtree(target_dir)
    os.mkdir(target_dir)
    shutil.copy(
        os.path.join(src_dir, "CMakeLists.txt"),
        os.path.join(target_dir, "CMakeLists.txt"),
    )
    shutil.copy(
        os.path.join(src_dir, ".clang-format"),
        os.path.join(target_dir, ".clang-format"),
    )
    shutil.copytree(
        os.path.join(src_dir, "pypp"),
        os.path.join(target_dir, "pypp"),
        dirs_exist_ok=True,
    )
