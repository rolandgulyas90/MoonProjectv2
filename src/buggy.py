class Buggy:
    def __init__(self, x: int, y: int, direction: str):
        self.x = x
        self.y = y
        self.direction = direction

    def move(self, command: str):
        if command == 'f' and self.direction == 'N':
            self.y -= 1
        elif command == 'f' and self.direction == 'S':
            self.y += 1