from dataclasses import dataclass
from pathlib import Path


def _create_pyproject_toml_deps(deps: list[str] | None) -> list[str]:
    if deps is None:
        return []
    middle_str = '    "' + '",\n    "'.join(deps) + '"'
    return ["dependencies = [", middle_str, "]"]


def create_python_hello_world(proj_dir: Path):
    hello_world: Path = proj_dir / "hello_world.py"
    hello_world.write_text(
        "\n".join(
            [
                "# Py++ src file example",
                "",
                "def hello_world_fn() -> str:",
                '    return "Hello, World!"',
            ]
        )
    )


@dataclass(frozen=True, slots=True)
class InitLibsHelper:
    _target_dir: Path
    _library_name: str

    def create_readme(self):
        readme: Path = self._target_dir / "readme.md"
        readme.write_text(f"# {self._library_name}\n")

    def create_pyproject_toml(
        self, library_name_underscores: str, dependencies: list[str] | None = None
    ):
        pyproject: Path = self._target_dir / "pyproject.toml"
        pyproject.write_text(
            "\n".join(
                [
                    "[project]",
                    f'name = "{self._library_name}"',
                    'version = "0.0.0"',
                    'description = ""',
                    "authors = []",
                    'readme = "readme.md"',
                    'license = {text = "MIT"}',
                    'requires-python = ">=3.13"',
                    *_create_pyproject_toml_deps(dependencies),
                    "",
                    "[tool.hatch.build]",
                    f'include = ["{library_name_underscores}/**/*"]',
                    "",
                    "[build-system]",
                    'requires = ["hatchling"]',
                    'build-backend = "hatchling.build"',
                ]
            )
        )
