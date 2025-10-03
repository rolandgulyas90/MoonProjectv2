class Buggy:
    def __init__(self, x: int, y: int, direction: str):
        self.x = x
        self.y = y
        self.direction = direction
        self._direction_vectors = {
            'N': (0, -1),
            'S': (0, 1),
            'E': (1, 0),
            'W': (-1, 0),
        }

    def move(self, command: str):
        vector = self._direction_vectors.get(self.direction)
        if not vector:
            return  # Ha ismeretlen az irány, ne csináljon semmit

        dx, dy = vector

        if command == 'f':
            self.x += dx
            self.y += dy
        elif command == 'b':
            self.x -= dx  # A vektor ellenkezőjét alkalmazzuk
            self.y -= dy  # A vektor ellenkezőjét alkalmazzuk
        elif command == 'l':
            if self.direction == 'N':
                self.direction = 'W'