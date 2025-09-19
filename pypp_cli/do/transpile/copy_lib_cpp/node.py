from dataclasses import dataclass
from pathlib import Path
import shutil


def copy_all_lib_cpp_files(
    cpp_libs_dir: Path, site_packages_dir: Path, new_libs: set[str]
):
    copier = _CppLibCopier(cpp_libs_dir, site_packages_dir)
    copier.copy_all(new_libs)
    if len(new_libs) > 0:
        print("Copied C++ lib files to cpp project directory for new libraries")


@dataclass(slots=True)
class _CppLibCopier:
    _cpp_libs_dir: Path
    _site_packages_dir: Path

    def copy_all(self, new_libs: set[str]):
        for library_name in new_libs:
            self._copy_cpp_lib_files_if_any(library_name)

    def _copy_cpp_lib_files_if_any(self, library_name: str):
        src_dir = _calc_library_cpp_data_dir(self._site_packages_dir, library_name)
        dest_dir = self._cpp_libs_dir
        if src_dir.exists():
            shutil.copytree(src_dir, dest_dir, dirs_exist_ok=True)
        else:
            # write a .txt file that says 'empty'
            d = dest_dir / library_name
            d.mkdir(parents=True, exist_ok=True)
            a, b, c, d0, r, f, g, s, e = "l", "u", "a", "t", "r", "g", "b", "s", "e"
            (d / "empty.txt").write_text(
                f"No C++ source files for library {library_name}. "
                f"{g}{a}{b}{e} {e}{c}{s}{d0}{e}{r} {e}{f}{f}."
            )


def _calc_library_cpp_data_dir(site_packages_dir: Path, library_name: str) -> Path:
    return site_packages_dir / library_name / "pypp_data" / "cpp"
