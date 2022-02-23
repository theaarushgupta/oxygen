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