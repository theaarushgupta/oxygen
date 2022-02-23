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

    def insert(self, cursor_: Any, string: str) -> None:
        row, column = cursor_.row, cursor_.column
        current = self.lines.pop(row)
        new = current[:column] + string + current[column:]
        self.lines.insert(row, new)