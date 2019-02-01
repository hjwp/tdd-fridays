from roman_number_calculator import add
import pytest


@pytest.mark.parametrize('first,second,expected', [
    ('I', 'I', 'II'),
    ('I', 'II', 'III'),
    ('II', 'I', 'III'),
    ('II', 'III', 'V'),
    ('I', 'V', 'VI'),
    ('V', 'I', 'VI'),
    ('V', 'V', 'X'),
    ('XXX', 'XX', 'L'),
    ('LX', 'VI', 'LXVI'),

])
def test_old_numerals(first, second, expected):
    assert add(first, second) == expected


@pytest.mark.parametrize('first,second,expected', [
    ('II', 'II', 'IV'),
    ('VIII', 'I', 'IX'),
    ('XXVIII', 'I', 'XXIX'),
])
def test_backwardsey_numerals_as_output(first, second, expected):
    assert add(first, second) == expected


@pytest.mark.parametrize('first,second,expected', [
    # ('V', 'IV', 'IX'),
])
def test_backwardsey_numerals_as_inputs(first, second, expected):
    assert add(first, second) == expected
