class Buggy:
    def __init__(self, x: int, y: int, direction: str):
        self.x = x
        self.y = y
        self.direction = direction

    def move(self, command: str):
        # Csak az 'f' parancsot kezeljük, és csak akkor, ha Észak felé nézünk
        if command == 'f' and self.direction == 'N':
            self.y -= 1