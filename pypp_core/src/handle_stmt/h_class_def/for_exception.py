import ast

from pypp_core.src.deps import Deps
from pypp_core.src.mapping.exceptions import lookup_cpp_exception_type


def handle_class_def_for_exception(
    node: ast.ClassDef,
    d: Deps,
) -> str:
    err_msg = "exception class body must only contain 'pass' statement"
    assert len(node.body) == 1, err_msg
    item = node.body[0]
    assert isinstance(item, ast.Pass), err_msg
    assert len(node.bases) == 1, "exception class must have exactly one base class"
    base = node.bases[0]
    assert isinstance(base, ast.Name), "exception class base must be a Name"
    name_doesnt_start_with_underscore: bool = not node.name.startswith("_")
    base_name = lookup_cpp_exception_type(base.id, d, name_doesnt_start_with_underscore)
    class_name = node.name
    return (
        f"class {class_name} : public {base_name}"
        + "{ public: explicit "
        + f"{class_name}(const std::string &msg) : {base_name}("
        + f'"{class_name}: " + msg)'
        + "{} };"
    )
