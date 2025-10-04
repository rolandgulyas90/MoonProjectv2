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
        if command == 'f' or command == 'b':
            vector = self._direction_vectors.get(self.direction)
            if not vector: return
            dx, dy = vector

            # Kiszámoljuk az új pozíciót, mielőtt frissítenénk az objektumot
            new_x = self.x
            new_y = self.y

            if command == 'f':
                new_x += dx
                new_y += dy
            elif command == 'b':
                new_x -= dx
                new_y -= dy

            # ÚJ: Gömb alakú pályaszélek kezelése
            # Szélességi körök (Y)
            if new_y < 0:
                self.y = self.planet.latitudes - 1
            else:
                self.y = new_y

            # Hosszúsági körök (X)
            if new_x >= self.planet.longitudes:
                self.x = 0
            elif new_x < 0:
                self.x = self.planet.longitudes - 1
            else:
                self.x = new_x

        elif command == 'l':
            self.direction = self._left_turn_map.get(self.direction, self.direction)
        elif command == 'r':
            self.direction = self._right_turn_map.get(self.direction, self.direction)