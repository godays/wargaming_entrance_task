import pytest
from qsort import sort_array


def test_can_sort_simple_array():
    arr = [4, 2, 1, 5]
    expected = [1, 2, 4, 5]
    sort_array(arr)
    assert expected == arr


def test_can_sort_reversed():
    arr = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    sort_array(arr)
    assert expected == arr


def test_can_sort_one_single_el():
    arr = [1]
    expected = [1]
    sort_array(arr)
    assert expected == arr
