from oxygen import buffer

class Cursor:
    def __init__(self, buffer_: buffer.Buffer, row: int = 0, column: int = 0) -> None:
        self.row = row
        self._column = column
        self.buffer = buffer_
        self._hint = column

    @property
    def column(self) -> int:
        return self._column

    @column.setter
    def column(self, column: int) -> None:
        self._column = self._hint = column

    def up(self) -> None:
        if self.row > 0:
            self.row -= 1
            self._clamp()

    def down(self) -> None:
        if self.row < self.buffer.bottom:
            self.row += 1
            self._clamp()

    def left(self) -> None:
        if self.column > 0:
            self.column -= 1
        elif self.row > 0:
            self.row -= 1
            self.column = len(self.buffer[self.row])

    def right(self) -> None:
        if self.column < len(self.buffer[self.row]):
            self.column += 1
        elif self.row < self.buffer.bottom:
            self.row += 1
            self.column = 0

    def _clamp(self) -> None:
        self._column = min(self._hint, len(self.buffer[self.row]))