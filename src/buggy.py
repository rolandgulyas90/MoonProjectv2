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
        elif command == 'r':
            self.direction = self._right_turn_map.get(self.direction, self.direction)
        elif command == 'f' or command == 'b':
            vector = self._direction_vectors.get(self.direction)
            if not vector:
                return
            dx, dy = vector

            # Hátramozgásnál megfordítjuk a vektort
            if command == 'b':
                dx, dy = -dx, -dy

            # Egységesített mozgás és átfordulás
            # A Python modulo operátora a negatív számokat is helyesen kezeli
            # Például: -1 % 10 = 9
            self.x = (self.x + dx) % self.planet.longitudes

            # A Y koordinátát a gömbpalást miatt egyedi logikával kell kezelni
            new_y = self.y + dy
            if new_y >= self.planet.latitudes:
                self.y = 0
            elif new_y < 0:
                self.y = self.planet.latitudes - 1
            else:
                self.y = new_y
