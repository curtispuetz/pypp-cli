def configclass(_cls=None, *, dtype=None):
    def wrap(cls):
        # If dtype is specified, assign type hints for all non-callable, non-dunder variables
        if dtype is not None:
            hints = {
                k: dtype
                for k, v in cls.__dict__.items()
                if not k.startswith("__") and not callable(v)
            }
            cls.__annotations__ = hints
        return cls

    # Support using decorator with and without parentheses
    if _cls is None:
        return wrap
    else:
        return wrap(_cls)
