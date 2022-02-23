from typing import Any # "from oxygen import cursor" causes circular import error

class Buffer:
    def __init__(self, lines: list) -> None:
        self.lines = lines

    def __len__(self) -> int:
        return len(self.lines)

    def __getitem__(self, index: int) -> str:
        return self.lines[index]

    @property
    def bottom(self) -> int:
        return len(self) - 1

    def insert(self, cursor: Any, string: str) -> None:
        row, column = cursor.row, cursor.column
        current = self.lines.pop(row)
        new = current[:column] + string + current[column:]
        self.lines.insert(row, new)

    def newline(self, cursor: Any) -> None:
        row, column = cursor.row, cursor.column
        current = self.lines.pop(row)
        self.lines.insert(row, current[:column])
        self.lines.insert(row + 1, current[column:])

    def delete(self, cursor: Any) -> None:
        row, column = cursor.row, cursor.column
        if (row, column) < (self.bottom, len(self[row])):
            current = self.lines.pop(row)
            if column < len(self[row]):
                new = current[:column] + current[column + 1:]
                self.lines.insert(row, new)
            else:
                next_ = self.lines.pop(row)
                new = current + next_
                self.lines.insert(row, new)