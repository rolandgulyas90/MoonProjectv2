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

def test_buggy_crosses_north_pole_and_changes_longitude():
    planet = Planet(latitudes=10, longitudes=10)
    # Kezdőpozíció: x=3, y=0 (legészakibb sor), irány Észak
    buggy = Buggy(x=3, y=0, direction='N', planet=planet)

    # Előre mozgás a sarkon át
    buggy.move('f')

    # Várt állapot:
    # y marad 0 (a sarkon)
    # az irány Délre vált
    # x a bolygó túloldalára kerül: (3 + 10/2) % 10 = 8
    expected_x = 8
    expected_y = 0
    expected_direction = 'S'

    assert buggy.y == expected_y, f"Várt y: {expected_y}, kapott: {buggy.y}"
    assert buggy.x == expected_x, f"Várt x: {expected_x}, kapott: {buggy.x}"
    assert buggy.direction == expected_direction, f"Várt irány: {expected_direction}, kapott: {buggy.direction}"


# FRISSÍTVE: A teszt a TELJES gömbmodellhez lett igazítva
def test_buggy_crosses_south_pole_and_changes_longitude():
    planet = Planet(latitudes=10, longitudes=10)
    # Kezdőpozíció: x=8, y=9 (legdélibb sor), irány Dél
    buggy = Buggy(x=8, y=9, direction='S', planet=planet)

    # Előre mozgás a sarkon át
    buggy.move('f')

    # Várt állapot:
    # y marad 9 (a sarkon)
    # az irány Északra vált
    # x a bolygó túloldalára kerül: (8 + 10/2) % 10 = 13 % 10 = 3
    expected_x = 3
    expected_y = 9
    expected_direction = 'N'

    assert buggy.y == expected_y, f"Várt y: {expected_y}, kapott: {buggy.y}"
    assert buggy.x == expected_x, f"Várt x: {expected_x}, kapott: {buggy.x}"
    assert buggy.direction == expected_direction, f"Várt irány: {expected_direction}, kapott: {buggy.direction}"