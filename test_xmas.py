from xmas import Grid

def test_default_count_is_zero():
    grid = Grid()
    assert grid.lit_count == 0

def test_turn_on_first_light():
    grid = Grid()
    command = "turn on 0,0 through 0,0"
    grid.act(command)
    assert grid.lit_count == 1









