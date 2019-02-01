from roman_number_calculator import add


def test_add_one_to_one():
    result = add('I', 'I')
    assert result == 'II'


def test_one_to_two():
    result = add('I', 'II')
    assert result == 'III'


def test_two_to_one():
    result = add('II', 'I')
    assert result == 'III'


def test_two_to_three():
    result = add('II', 'III')
    assert result == 'V'


def test_one_to_five():
    result = add('I', 'V')
    assert result == 'VI'

