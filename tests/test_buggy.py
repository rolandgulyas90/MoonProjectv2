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