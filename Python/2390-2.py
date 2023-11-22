# Removing Stars From a String
# Medium

from functools import reduce

def removeStars(s: str) -> str:
    return reduce(
        lambda r, c: ( r + c, r[:-1] )[c == '*'], s, ''
    )