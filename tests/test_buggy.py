# tests/test_buggy.py
from src.buggy import Buggy
from src.planet import Planet


def test_buggy_initialization():
    start_x = 5
    start_y = 5
    start_direction = 'N'
    planet = Planet(latitudes=10, longitudes=10)
    buggy = Buggy(x=start_x, y=start_y, direction=start_direction, planet=planet)

    assert buggy.x == start_x
    assert buggy.y == start_y
    assert buggy.direction == start_direction
    assert buggy.planet == planet


def test_buggy_moves_forward_when_facing_north():
    planet = Planet(latitudes=10, longitudes=10)
    buggy = Buggy(x=5, y=5, direction='N', planet=planet)
    expected_x = 5
    expected_y = 4

    buggy.move('f')

    assert buggy.x == expected_x
    assert buggy.y == expected_y
    assert buggy.direction == 'N'


def test_buggy_moves_forward_when_facing_south():
    planet = Planet(latitudes=10, longitudes=10)
    buggy = Buggy(x=5, y=5, direction='S', planet=planet)
    expected_x = 5
    expected_y = 6

    buggy.move('f')

    assert buggy.x == expected_x
    assert buggy.y == expected_y
    assert buggy.direction == 'S'


def test_buggy_moves_forward_when_facing_east():
    planet = Planet(latitudes=10, longitudes=10)
    buggy = Buggy(x=5, y=5, direction='E', planet=planet)
    expected_x = 6
    expected_y = 5

    buggy.move('f')

    assert buggy.x == expected_x
    assert buggy.y == expected_y
    assert buggy.direction == 'E'


def test_buggy_moves_forward_when_facing_west():
    planet = Planet(latitudes=10, longitudes=10)
    buggy = Buggy(x=5, y=5, direction='W', planet=planet)
    expected_x = 4
    expected_y = 5

    buggy.move('f')

    assert buggy.x == expected_x
    assert buggy.y == expected_y
    assert buggy.direction == 'W'


def test_buggy_moves_backward_when_facing_north():
    planet = Planet(latitudes=10, longitudes=10)
    buggy = Buggy(x=5, y=5, direction='N', planet=planet)
    expected_x = 5
    expected_y = 6

    buggy.move('b')

    assert buggy.x == expected_x
    assert buggy.y == expected_y
    assert buggy.direction == 'N'


def test_buggy_moves_backward_when_facing_south():
    planet = Planet(latitudes=10, longitudes=10)
    buggy = Buggy(x=5, y=5, direction='S', planet=planet)

    buggy.move('b')

    assert buggy.x == 5
    assert buggy.y == 4
    assert buggy.direction == 'S'


def test_buggy_moves_backward_when_facing_east():
    planet = Planet(latitudes=10, longitudes=10)
    buggy = Buggy(x=5, y=5, direction='E', planet=planet)

    buggy.move('b')

    assert buggy.x == 4
    assert buggy.y == 5
    assert buggy.direction == 'E'


def test_buggy_moves_backward_when_facing_west():
    planet = Planet(latitudes=10, longitudes=10)
    buggy = Buggy(x=5, y=5, direction='W', planet=planet)

    buggy.move('b')

    assert buggy.x == 6
    assert buggy.y == 5
    assert buggy.direction == 'W'


def test_buggy_turns_left_from_north_to_west():
    planet = Planet(latitudes=10, longitudes=10)
    buggy = Buggy(x=5, y=5, direction='N', planet=planet)

    buggy.move('l')

    assert buggy.x == 5
    assert buggy.y == 5
    assert buggy.direction == 'W'


def test_buggy_turns_left_from_west_to_south():
    planet = Planet(latitudes=10, longitudes=10)
    buggy = Buggy(x=5, y=5, direction='W', planet=planet)

    buggy.move('l')

    assert buggy.x == 5
    assert buggy.y == 5
    assert buggy.direction == 'S'


def test_buggy_turns_left_from_south_to_east():
    planet = Planet(latitudes=10, longitudes=10)
    buggy = Buggy(x=5, y=5, direction='S', planet=planet)

    buggy.move('l')

    assert buggy.x == 5
    assert buggy.y == 5
    assert buggy.direction == 'E'


def test_buggy_turns_left_from_east_to_north():
    planet = Planet(latitudes=10, longitudes=10)
    buggy = Buggy(x=5, y=5, direction='E', planet=planet)

    buggy.move('l')

    assert buggy.x == 5
    assert buggy.y == 5
    assert buggy.direction == 'N'


def test_buggy_turns_right_from_north_to_east():
    planet = Planet(latitudes=10, longitudes=10)
    buggy = Buggy(x=5, y=5, direction='N', planet=planet)

    buggy.move('r')

    assert buggy.x == 5
    assert buggy.y == 5
    assert buggy.direction == 'E'


def test_buggy_turns_right_from_east_to_south():
    planet = Planet(latitudes=10, longitudes=10)
    buggy = Buggy(x=5, y=5, direction='E', planet=planet)

    buggy.move('r')

    assert buggy.x == 5
    assert buggy.y == 5
    assert buggy.direction == 'S'


def test_buggy_turns_right_from_south_to_west():
    planet = Planet(latitudes=10, longitudes=10)
    buggy = Buggy(x=5, y=5, direction='S', planet=planet)

    buggy.move('r')

    assert buggy.x == 5
    assert buggy.y == 5
    assert buggy.direction == 'W'


def test_buggy_turns_right_from_west_to_north():
    planet = Planet(latitudes=10, longitudes=10)
    buggy = Buggy(x=5, y=5, direction='W', planet=planet)

    buggy.move('r')

    assert buggy.x == 5
    assert buggy.y == 5
    assert buggy.direction == 'N'

# FRISSÍTVE: A teszt a gömbmodellhez lett igazítva
def test_buggy_wraps_around_the_north_pole():
    planet = Planet(latitudes=10, longitudes=10)
    buggy = Buggy(x=5, y=0, direction='N', planet=planet)

    buggy.move('f')

    assert buggy.y == 0
    assert buggy.x == 5
    assert buggy.direction == 'S'

# FRISSÍTVE: A teszt a gömbmodellhez lett igazítva
def test_buggy_wraps_around_the_south_pole():
    planet = Planet(latitudes=10, longitudes=10)
    buggy = Buggy(x=5, y=9, direction='S', planet=planet)

    buggy.move('f')

    assert buggy.y == 9
    assert buggy.x == 5
    assert buggy.direction == 'N'