class Planet:
    def __init__(self, latitudes: int, longitudes: int, obstacles: list[tuple[int, int]] | None = None):
        """
        Inicializál egy bolygót a megadott méretekkel és akadályokkal.

        Args:
            latitudes: A szélességi fokok száma (y tengely mérete).
            longitudes: A hosszúsági fokok száma (x tengely mérete).
            obstacles: Az akadályok listája, ahol minden akadály egy (x, y) koordináta.
        """
        self.latitudes = latitudes
        self.longitudes = longitudes
        self.obstacles = set(obstacles) if obstacles else set()

    def has_obstacle(self, x: int, y: int) -> bool:
        """
        Ellenőrzi, hogy a megadott koordinátán található-e akadály.
        """
        return (x, y) in self.obstacles