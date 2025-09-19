from pathlib import Path
from dataclasses import dataclass

from pypp_cli.do.transpile.find_libs.z.other.find_all_libs import PyppLibs


def find_new_libs(cpp_dir: Path, libs: PyppLibs) -> set[str]:
    f = _Finder(cpp_dir, libs)
    return f.find()


def _print_new_libraries(new):
    print("New libraries:", new)


@dataclass(frozen=True, slots=True)
class _Finder:
    cpp_dir: Path
    libs: PyppLibs

    def find(self) -> set[str]:
        libs_dir: Path = self.cpp_dir / "libs"
        if not libs_dir.is_dir():
            new = list(self.libs.keys())
            _print_new_libraries(new)
            return set(self.libs.keys())
        new = set(self.libs.keys())
        for entry in libs_dir.iterdir():
            if entry.is_dir():
                if entry.name in self.libs:
                    new.discard(entry.name)
        _print_new_libraries(list(new))
        return new
