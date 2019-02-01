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
    # ('V', 'IV', 'IX'),
])
def test_backwardsey_numerals(first, second, expected):
    assert add(first, second) == expected
