class Buggy:
    def __init__(self, x: int, y: int, direction: str):
        self.x = x
        self.y = y
        self.direction = direction
        self._direction_vectors = {
            'N': (0, -1),
            'S': (0, 1),
            'E': (1, 0),
        }

    def move(self, command: str):
        if command == 'f':
            # Kikeresi a jelenlegi irányhoz tartozó vektort
            vector = self._direction_vectors.get(self.direction)

            if vector:
                dx, dy = vector
                self.x += dx
                self.y += dy