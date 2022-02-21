from oxygen import cursor

class Window:
    def __init__(
        self,
        buffer: list,
        cursor_: cursor.Cursor,
        rowCount: int,
        columnCount: int,
        row: int = 0,
        column: int = 0
    ) -> None:
        self.buffer = buffer
        self.cursor = cursor_
        self.rowCount = rowCount
        self.columnCount = columnCount
        self.row = row
        self.column = column

    @property
    def bottom(self) -> int:
        return self.row + self.rowCount - 1

    def up(self) -> None:
        if self.cursor.row == self.row - 1 and self.row > 0:
            self.row -= 1

    def down(self) -> None:
        if self.cursor.row == self.bottom + 1 and self.bottom < len(self.buffer) - 1:
            self.row += 1

    def translate(self) -> tuple:
        return self.cursor.row - self.row, self.cursor.column - self.column