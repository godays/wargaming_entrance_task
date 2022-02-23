from __future__ import annotations


def isEven(value: int) -> bool:
    """check if value is even
        converts the value to a binary form and checks the last digit
        1 == odd
        0 == even
    """
    return bin(value)[-1] == '0'
