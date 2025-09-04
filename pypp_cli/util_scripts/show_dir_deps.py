import ast
from pathlib import Path

# Config
target_module = "transpilers.other.transpiler"


# Implementation
full_target_module = "pypp_cli.src." + target_module
proj_root_dir: Path = Path(r"/pypp_cli\src")

target_dir: Path = proj_root_dir
for part in target_module.split("."):
    target_dir /= part


def calc_all_py_files_ignoring(root: Path, ignore: Path) -> list[Path]:
    ret: list[Path] = []
    # TODO later: change to depth first search because that output is prefered.
    for path in root.rglob("*.py"):
        if ignore not in path.parents:
            ret.append(path.relative_to(root))
    return ret


py_files = calc_all_py_files_ignoring(proj_root_dir, target_dir)

for py_file in py_files:
    py_code: str = (proj_root_dir / py_file).read_text()
    ast_tree = ast.parse(py_code)
    assert isinstance(ast_tree, ast.Module), "Shouldn't happen"
    for stmt in ast_tree.body:
        if isinstance(stmt, ast.Import):
            continue
        if isinstance(stmt, ast.ImportFrom):
            assert stmt.module is not None, "Not supported"
            if stmt.module.startswith(full_target_module):
                res = str(py_file)
                print(res, " " * (70 - len(res)) + stmt.module)
                break  # So you don't print the same twice
        else:
            break
