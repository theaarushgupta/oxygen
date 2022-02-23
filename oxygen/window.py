from oxygen import buffer
from oxygen import cursor

class Window:
    def __init__(
        self,
        buffer_: buffer.Buffer,
        cursor_: cursor.Cursor,
        rowCount: int,
        columnCount: int,
        row: int = 0,
        column: int = 0
    ) -> None:
        self.buffer = buffer_
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
        if self.cursor.row == self.bottom + 1 and self.bottom < self.buffer.bottom:
            self.row += 1

    def translate(self) -> tuple:
        return self.cursor.row - self.row, self.cursor.column - self.column

    def horizontalScroll(self, left: int = 5, right: int = 5) -> None:
        pages = self.cursor.column // (self.columnCount - right)
        self.column = max(pages * self.columnCount - right - left, 0)