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

    def move(self, command: str) -> bool | str:
        if command in ('l', 'r'):
            if command == 'l':
                self.direction = self._left_turn_map.get(self.direction, self.direction)
            else:  # command == 'r'
                self.direction = self._right_turn_map.get(self.direction, self.direction)
            return True

        if command in ('f', 'b'):
            # 1. Célkoordináták meghatározása (Calculate)
            vector = self._direction_vectors.get(self.direction, (0, 0))
            dx, dy = (-vector[0], -vector[1]) if command == 'b' else vector

            potential_y = self.y + dy

            final_x, final_y, final_dir = self.x, self.y, self.direction

            if potential_y < 0:  # Északi-sark
                final_y = 0
                final_x = (self.x + self.planet.longitudes // 2) % self.planet.longitudes
                final_dir = 'S'
            elif potential_y >= self.planet.latitudes:  # Déli-sark
                final_y = self.planet.latitudes - 1
                final_x = (self.x + self.planet.longitudes // 2) % self.planet.longitudes
                final_dir = 'N'
            else:  # Normál mozgás
                final_y = potential_y
                final_x = (self.x + dx) % self.planet.longitudes

            # 2. Ellenőrzés egyetlen helyen (Check)
            if self.planet.has_obstacle(final_x, final_y):
                return "AKADÁLY"

            # 3. Végrehajtás (Commit)
            self.x, self.y, self.direction = final_x, final_y, final_dir
            return True

        return True  # Ismeretlen parancs esetén is sikeresnek vesszük