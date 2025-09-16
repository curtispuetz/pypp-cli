from .basic_info import validate_required_py_import


def validate_2(o: object, S: str):
    assert isinstance(o, dict), f"{S} must be a JSON object"
    for k, v in o.items():
        assert isinstance(k, str), f"Key in {S} must be a string"
        assert v is None or isinstance(v, dict), (
            f"Entry for {k} in {S} must be a JSON object or null"
        )
        if isinstance(v, dict):
            assert "required_py_import" in v, (
                f"Entry for {k} in {S} must have a 'required_py_import' key or be null"
            )
            assert len(v) == 1, f"Entry for {k} in {S} must have exactly one key"
            validate_required_py_import([k], v["required_py_import"], S)
