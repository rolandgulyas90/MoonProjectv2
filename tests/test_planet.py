from src.planet import Planet

def test_planet_creation():
    expected_latitudes = 10
    expected_longitudes = 10

    planet = Planet(latitudes = expected_latitudes, longitudes = expected_longitudes)

    assert planet.latitudes == expected_latitudes
    assert planet.longitudes == expected_longitudes