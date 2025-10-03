class Buggy:
    def __init__(self, x: int, y: int, direction: str):
        self.x = x
        self.y = y
        self.direction = direction

        self._direction_vectors = {
            'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0),
        }

        # ÚJ: Szótár a balra forduláshoz
        self._left_turn_map = {
            'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N',
        }
        # ÚJ: Szótár a jobbra forduláshoz (ezt majd később használjuk)
        self._right_turn_map = {
            'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N',
        }

    def move(self, command: str):
        if command == 'f' or command == 'b':
            vector = self._direction_vectors.get(self.direction)
            if not vector: return
            dx, dy = vector

            if command == 'f':
                self.x += dx
                self.y += dy
            elif command == 'b':
                self.x -= dx
                self.y -= dy

        # ÁTÍRVA: A fordulás logikája mostantól egy szótárat használ
        elif command == 'l':
            self.direction = self._left_turn_map.get(self.direction, self.direction)