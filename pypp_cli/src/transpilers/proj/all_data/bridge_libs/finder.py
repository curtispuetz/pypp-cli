from pathlib import Path
from dataclasses import dataclass

from pypp_cli.src.transpilers.library.bridge_libs.finder import PyppLibs


def find_added_and_deleted_libs(
    cpp_dir: Path, libs: PyppLibs
) -> tuple[set[str], list[str]]:
    f = _Finder(cpp_dir, libs)
    return f.find()


def _print_results(new: list[str], deleted: list[str]):
    _print_new_libraries(new)
    print("Deleted libraries:", deleted)


def _print_new_libraries(new):
    print("New pure libraries:", new)


@dataclass(frozen=True, slots=True)
class _Finder:
    cpp_dir: Path
    libs: PyppLibs

    def find(self) -> tuple[set[str], list[str]]:
        libs_dir: Path = self.cpp_dir / "libs"
        if not libs_dir.is_dir():
            new = list(self.libs.keys())
            _print_new_libraries(new)
            return set(self.libs.keys()), []
        new = set(self.libs.keys())
        deleted = []
        for entry in libs_dir.iterdir():
            if entry.is_dir():
                if entry.name not in self.libs:
                    deleted.append(entry.name)
                else:
                    new.discard(entry.name)
        _print_results(list(new), deleted)
        return new, deleted
