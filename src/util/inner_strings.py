def calc_inside_rd(s: str):
    return _calc_inner_str(s, "(")


def calc_inside_sq(s: str):
    return _calc_inner_str(s, "[")


def calc_inside_ang(s: str):
    return _calc_inner_str(s, "<")


def _calc_inner_str(s: str, inner_char: str) -> str:
    return s.split(inner_char, 1)[1][:-1]
