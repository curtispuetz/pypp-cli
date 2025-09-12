def _void_fn():
    for i in range(3):
        if i == 1:
            print("finished")
            return


def empty_return_fn():
    print("EMPTY RETURN RESULTS:")
    _void_fn()
