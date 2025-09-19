import os
import shutil

dirname: str = os.path.dirname(__file__)

if __name__ == "__main__":
    src_dir = os.path.join(dirname, "..", "..", "..", "Projects", "cpp_playground")
    assert os.path.isdir(src_dir), "src_dir is not a dir"
    target_dir = os.path.join(dirname, "..", "data", "cpp_template")
    target_dir_2 = os.path.join(dirname, "..", "test_dir", "cpp")
    shutil.rmtree(target_dir)
    os.mkdir(target_dir)
    shutil.copy(
        os.path.join(src_dir, ".clang-format"),
        os.path.join(target_dir, ".clang-format"),
    )
    shutil.copytree(
        os.path.join(src_dir, "pypp"),
        os.path.join(target_dir, "pypp"),
        dirs_exist_ok=True,
    )
    shutil.copytree(
        os.path.join(src_dir, "pypp"),
        os.path.join(target_dir_2, "pypp"),
        dirs_exist_ok=True,
    )
