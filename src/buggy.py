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

            if command == 'b':
                dx, dy = -dx, -dy

            new_x = (self.x + dx) % self.planet.longitudes
            new_y = self.y + dy

            # ÚJ GÖMBMODELL LOGIKA
            if new_y < 0:
                # Északi pólus átlépése
                self.y = 0  # Marad a 0-ás sorban
                # Az irány 180 fokkal megfordul (N -> S, S -> N)
                if self.direction == 'N':
                    self.direction = 'S'
                elif self.direction == 'S':
                    self.direction = 'N'
                # A hosszúsági (X) koordinátát is módosítanunk kell a gömbön,
                # de a mostani tesztünk nem kéri. Ez a refaktor fázis feladata lehet.
            elif new_y >= self.planet.latitudes:
                # Déli pólus átlépése
                self.y = self.planet.latitudes - 1  # Marad a szélen
                if self.direction == 'S':
                    self.direction = 'N'
                elif self.direction == 'N':
                    self.direction = 'S'
            else:
                self.y = new_y

            # A hosszúsági koordináta most is a moduló logikával működik
            self.x = (self.x + dx) % self.planet.longitudes
