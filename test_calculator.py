from roman_number_calculator import add


def test_add_one_to_one_no_class():
    result = add('I', 'I')
    assert result == 'II'


def test_one_to_two_no_class():
    result = add('I', 'II')
    assert result == 'III'
