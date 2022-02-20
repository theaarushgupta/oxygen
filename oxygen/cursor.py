class Cursor:
    def __init__(self, row: int = 0, column: int = 0) -> None:
        self.row = row
        self.column = column

    def up(self): self.row -= 1
    def down(self): self.row += 1
    def left(self): self.column -= 1
    def right(self): self.column += 1