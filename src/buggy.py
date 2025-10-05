from src.planet import Planet

class Buggy:
    def __init__(self, x: int, y: int, direction: str, planet: Planet):
        self.x = x
        self.y = y
        self.direction = direction
        self.planet = planet

        self._direction_vectors = {
            'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0),
        }

        self._left_turn_map = {
            'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N',
        }
        self._right_turn_map = {
            'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N',
        }

    def move(self, command: str):
        if command == 'l':
            self.direction = self._left_turn_map.get(self.direction, self.direction)
            return # A return ide is kell a konzisztencia miatt
        elif command == 'r':
            self.direction = self._right_turn_map.get(self.direction, self.direction)
            return # és ide is

        if command == 'f' or command == 'b':
            vector = self._direction_vectors.get(self.direction)
            if not vector:
                return
            dx, dy = vector

            if command == 'b':
                dx, dy = -dx, -dy

            # Kiszámoljuk a leendő pozíciót
            new_x = self.x + dx
            new_y = self.y + dy

            # Kezeljük a sarkokat a teljes gömb-logika szerint
            if new_y < 0:  # Északi-sark átlépése
                self.y = 0
                self.direction = 'S'
                self.x = (self.x + self.planet.longitudes // 2) % self.planet.longitudes
            elif new_y >= self.planet.latitudes:  # Déli-sark átlépése
                self.y = self.planet.latitudes - 1
                self.direction = 'N'
                self.x = (self.x + self.planet.longitudes // 2) % self.planet.longitudes
            else:  # Normál mozgás a bolygó "palástján"
                self.y = new_y
                self.x = new_x % self.planet.longitudes
