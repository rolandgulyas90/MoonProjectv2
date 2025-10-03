from src.buggy import Buggy

def test_buggy_initialization():
    start_x = 5
    start_y = 5
    start_direction = 'N'

    buggy = Buggy(x=start_x, y=start_y, direction=start_direction)

    assert buggy.x == start_x
    assert buggy.y == start_y
    assert buggy.direction == start_direction

def test_buggy_moves_forward_when_facing_north():
    # Létrehozunk egy Buggy-t, ami észak felé néz
    buggy = Buggy(x=5, y=5, direction='N')
    expected_x = 5
    expected_y = 4 # Észak felé haladva az Y koordináta csökken

    # Adunk neki egy 'f' (forward) parancsot
    buggy.move('f')

    # Ellenőrizzük, hogy a pozíciója megváltozott-e a vártnak megfelelően
    assert buggy.x == expected_x
    assert buggy.y == expected_y
    assert buggy.direction == 'N' # Az iránynak nem szabad változnia

def test_buggy_moves_forward_when_facing_south():
    # Létrehozunk egy Buggy-t, ami dél felé néz
    buggy = Buggy(x=5, y=5, direction='S')
    expected_x = 5
    expected_y = 6 # Dél felé haladva az Y koordináta nő

    buggy.move('f')

    # Ellenőrizzük, hogy a pozíciója megváltozott-e a vártnak megfelelően
    assert buggy.x == expected_x
    assert buggy.y == expected_y
    assert buggy.direction == 'S'

def test_buggy_moves_forward_when_facing_east():
    buggy = Buggy(x=5, y=5, direction='E')
    expected_x = 6 # Kelet felé haladva az X koordináta nő
    expected_y = 5

    buggy.move('f')

    assert buggy.x == expected_x
    assert buggy.y == expected_y
    assert buggy.direction == 'E'

def test_buggy_moves_forward_when_facing_west():
    buggy = Buggy(x=5, y=5, direction='W')
    expected_x = 4 # Nyugat felé haladva az X koordináta csökken
    expected_y = 5

    buggy.move('f')

    assert buggy.x == expected_x
    assert buggy.y == expected_y
    assert buggy.direction == 'W'

def test_buggy_moves_backward_when_facing_north():
    buggy = Buggy(x=5, y=5, direction='N')
    expected_x = 5
    expected_y = 6 # Hátra észak felől = Dél felé mozgás

    buggy.move('b')

    assert buggy.x == expected_x
    assert buggy.y == expected_y
    assert buggy.direction == 'N'


def test_buggy_turns_left_from_north_to_west():
    buggy = Buggy(x=5, y=5, direction='N')

    buggy.move('l')

    assert buggy.x == 5  # A pozíció nem változik
    assert buggy.y == 5
    assert buggy.direction == 'W'  # Az iránynak 'W'-re kell változnia


def test_buggy_turns_left_from_west_to_south():
    buggy = Buggy(x=5, y=5, direction='W')

    buggy.move('l')

    assert buggy.x == 5
    assert buggy.y == 5
    assert buggy.direction == 'S'


def test_buggy_turns_left_from_south_to_east():
    buggy = Buggy(x=0, y=0, direction='S')

    buggy.move('l')

    assert buggy.direction == 'E'


def test_buggy_turns_left_from_east_to_north():
    buggy = Buggy(x=0, y=0, direction='E')

    buggy.move('l')

    assert buggy.direction == 'N'