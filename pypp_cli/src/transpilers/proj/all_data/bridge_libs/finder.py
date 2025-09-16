from pathlib import Path
from dataclasses import dataclass


def find_added_and_deleted_libs(
    cpp_dir: Path, bridge_libs: list[str], pure_libs: list[str]
) -> tuple[list[str], list[str], list[str]]:
    f = _Finder(cpp_dir, bridge_libs, pure_libs)
    return f.find()


@dataclass(frozen=True, slots=True)
class _Finder:
    cpp_dir: Path
    bridge_libs: list[str]
    pure_libs: list[str]

    def find(self) -> tuple[list[str], list[str], list[str]]:
        libs_dir: Path = self.cpp_dir / "libs"
        if not libs_dir.is_dir():
            self._print_no_libs_dir()
            return self.bridge_libs, self.pure_libs, []
        bridge_libs_set = set(self.bridge_libs)
        pure_libs_set = set(self.pure_libs)
        added_bridge = bridge_libs_set.copy()
        added_pure = pure_libs_set.copy()
        deleted = []
        for entry in libs_dir.iterdir():
            if entry.is_dir():
                if (
                    entry.name not in bridge_libs_set
                    and entry.name not in pure_libs_set
                ):
                    deleted.append(entry.name)
                else:
                    added_bridge.discard(entry.name)
                    added_pure.discard(entry.name)
        ret_bridge = list(added_bridge)
        ret_pure = list(added_pure)
        self._print_results(ret_bridge, ret_pure, deleted)
        return ret_bridge, ret_pure, deleted

    def _print_results(
        self, ret_bridge: list[str], ret_pure: list[str], deleted: list[str]
    ):
        print("Found bridge libraries:", self.bridge_libs)
        print("New bridge libraries:", ret_bridge)
        print("Found pure libraries:", self.pure_libs)
        print("New pure libraries:", ret_pure)
        print("Deleted libraries:", deleted)

    def _print_no_libs_dir(self):
        print("Found bridge libraries:", self.bridge_libs)
        print("New pure libraries:", self.pure_libs)
