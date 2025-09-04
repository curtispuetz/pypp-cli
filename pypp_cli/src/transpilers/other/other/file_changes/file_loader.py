from pathlib import Path


def calc_all_py_files(root: Path) -> list[Path]:
    ret: list[Path] = []
    for path in root.rglob("*.py"):
        ret.append(path.relative_to(root))
    return ret
