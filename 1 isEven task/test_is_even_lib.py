import pytest
import is_even_lib


def test_work_correctly_for_odd():
    expected = False
    result = is_even_lib.isEven(5)
    assert expected == result


def test_work_correctly_for_even():
    expected = True
    result = is_even_lib.isEven(4)
    assert expected == result
