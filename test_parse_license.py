import pytest

from parse_license import parse, parse_one

def test_no_children_sums_metadata():
    assert parse('0 3 4 5 6') == 4 + 5 + 6
    assert parse('0 2 0 7') == 7


def test_one_child():
    assert parse('1 2 0 1 9 2 7') == 18

@pytest.mark.xfail
def test_two_child():
    assert parse('2 2 0 1 9 0 3 6 6 6 2 7') == 9 + 6+6+6 + 2+7

def test_parse_one_for_no_children():
    assert parse_one([0, 3, 4, 5, 6, 7, 8, 9]) == (4 + 5 + 6, [7, 8, 9])
    assert parse_one([0, 3, 5, 6, 7, 8, 9, 10]) == (5 + 6 + 7, [8, 9, 10])
