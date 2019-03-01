from parse_license import parse

def test_no_children_sums_metadata():
    assert parse('0 3 4 5 6') == 4 + 5 + 6
    assert parse('0 2 0 7') == 7


def test_one_child():
    assert parse('1 2 0 1 9 2 7') == 18
