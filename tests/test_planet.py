from src.planet import Planet

def test_planet_creation():
    expected_latitudes = 10
    expected_longitudes = 10

    planet = Planet(latitudes = expected_latitudes, longitudes = expected_longitudes)

    assert planet.latitudes == expected_latitudes
    assert planet.longitudes == expected_longitudes


def test_planet_stores_obstacles():
    """Teszteli, hogy a bolygó helyesen tárolja-e az akadályokat."""
    obstacles = [(1, 2), (3, 4)]
    planet = Planet(latitudes=10, longitudes=10, obstacles=obstacles)

    # A set használata hatékonyabbá teszi a későbbi keresést
    assert planet.obstacles == set(obstacles)


def test_planet_can_identify_obstacle_location():
    """Teszteli, hogy a bolygó meg tudja-e mondani egy koordinátáról, hogy van-e ott akadály."""
    obstacles = [(1, 2), (3, 4)]
    planet = Planet(latitudes=10, longitudes=10, obstacles=obstacles)

    assert planet.has_obstacle(1, 2) is True
    assert planet.has_obstacle(3, 4) is True
    assert planet.has_obstacle(5, 5) is False  # Ezen a helyen nincs akadály