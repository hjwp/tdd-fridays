from xmas import Grid


def test_default_count_is_zero():
    grid = Grid()
    assert grid.lit_count == 0

def test_turn_on_first_light():
    grid = Grid()
    command = "turn on 0,0 through 0,0"
    grid.act(command)
    assert grid.lit_count == 1

def test_off_on_first_light():
    grid = Grid()
    command = "turn off 0,0 through 0,0"
    grid.act(command)
    assert grid.lit_count == 0
    grid.act("turn on 0,0 through 0,0")
    grid.act("turn off 0,0 through 0,0")
    assert grid.lit_count == 0

def test_toggle_first_light():
    grid = Grid()
    command = "turn on 0,0 through 0,0"
    grid.act(command)
    assert grid.lit_count == 1
    command = "toggle 0,0 through 0,0"
    grid.act(command)
    assert grid.lit_count == 0
    command = "toggle 0,0 through 0,0"
    grid.act(command)
    assert grid.lit_count == 1

def test_turn_on_two_lights_in_a_range():
    grid = Grid()
    grid.act("turn on 0,0 through 0,1")
    assert grid.lit_count == 2

def test_turn_on_line_longer_than_2():
    grid = Grid()
    grid.act("turn on 0,0 through 0,3")
    assert grid.lit_count == 4
