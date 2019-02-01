from roman_number_calculator import add


def test_add_i_to_i():
    result = add('I', 'I')
    assert result == 'II'

def test_i_to_ii():
    result = add('I', 'II')
    assert result == 'III'

def test_ii_to_i():
    result = add('II', 'I')
    assert result == 'III'

def test_ii_to_ii():
    result = add('II', 'II')
    assert result == 'IIII'  # TODO: support modern roman numerals one day

def test_ii_to_iii():
    result = add('II', 'III')
    assert result == 'V'

def test_i_to_v():
    result = add('I', 'V')
    assert result == 'VI'
    result = add('V', 'I')
    assert result == 'VI'

def test_v_to_v():
    result = add('V', 'V')
    assert result == 'X'

def test_add_xxx_to_xx():
    result = add('XXX', 'XX')
    assert result == 'L'

def test_add_lx_to_vi():
    result = add('LX', 'VI')
    assert result == 'LXVI'
