from roman_number_calculator import Calculator


def test_add_one_to_one():
    calc = Calculator()
    result = calc.add('I', 'I')
    assert result == 'II'


def test_one_to_two():
    calc = Calculator()
    result = calc.add('I', 'II')
    assert result == 'III'
