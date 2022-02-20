class Cursor:
    def __init__(self, buffer: list, row: int = 0, column: int = 0) -> None:
        self.row = row
        self.column = column
        self.buffer = buffer

    def up(self):
        if self.row > 0:
            self.row -= 1

    def down(self):
        if self.row < len(self.buffer) - 1:
            self.row += 1

    def left(self):
        if self.column > 0:
            self.column -= 1

    def right(self):
        if self.column < len(self.buffer[self.row]):
            self.column += 1