from pypp_core.src.d_types import (
    PySpecificImport,
    AngInc,
    QInc,
    PySpecificImpFrom,
    PyImport,
    CppInclude,
)


def calc_cpp_includes(obj: dict) -> list[CppInclude]:
    ret: list[CppInclude] = []
    if "cpp_includes" in obj:
        assert isinstance(obj["cpp_includes"], dict), "cpp_includes must be an object"
        for inc_type, inc_str in obj["cpp_includes"].items():
            if inc_type == "quote_include":
                ret.append(QInc(inc_str))
            elif inc_type == "angle_include":
                ret.append(AngInc(inc_str))
            else:
                raise ValueError(f"invalid type in cpp_includes object: {inc_type}")
    return ret


def calc_required_py_import(obj: dict) -> PySpecificImport | None:
    if "required_py_import" in obj:
        req = obj["required_py_import"]
        assert isinstance(req, dict), "required_py_import must be an object"
        assert "name" in req, "required_py_import must specify a name"
        if "module" in req:
            return PySpecificImpFrom(req["module"], req["name"])
        if "as_name" in req:
            return PyImport(req["name"], req["as_name"])
        return PyImport(req["name"])
    return None
