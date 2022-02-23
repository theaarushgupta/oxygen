import curses
import sys
import argparse

from oxygen import file
from oxygen import window
from oxygen import cursor
from oxygen import color

class Oxygen:
    def __init__(self, screen: "curses._CursesWindow", filename: str) -> None:
        self.screen = screen
        self.buffer = file.load(filename)
        self.cursor = cursor.Cursor(self.buffer)
        self.window = window.Window(self.buffer, self.cursor, curses.LINES - 1, curses.COLS - 1)
        self.color = color.Color(self.screen)
        self.color.apply(self.color.create(1))
        self.entry()

    def draw(self) -> None:
        self.screen.erase()
        for row, line in enumerate(self.buffer[self.window.row:self.window.row + self.window.rowCount]):
            if row == self.cursor.row - self.window.row and self.window.column > 0:
                line = "«" + line[self.window.column + 1:]
            if len(line) > self.window.columnCount:
                line = line[:self.window.columnCount - 1] + "»"
            self.screen.addstr(row, 0, line)
        self.screen.move(*self.window.translate())

    def _exit(self) -> None: sys.exit(0)

    def up(self) -> None:
        self.cursor.up()
        self.window.up()
        self.window.horizontalScroll()

    def down(self) -> None:
        self.cursor.down()
        self.window.down()
        self.window.horizontalScroll()

    def left(self) -> None:
        self.cursor.left()
        self.window.up()
        self.window.horizontalScroll()

    def right(self) -> None:
        self.cursor.right()
        self.window.down()
        self.window.horizontalScroll()

    def insert(self, key: str) -> None:
        if key == "\n":
            self.buffer.newline(self.cursor)
            self.right()
        elif key in ("KEY_DC", "KEY_DELETE", "\x04"):
            self.buffer.delete(self.cursor)
        elif key in ("KEY_BACKSPACE", "\x7f"):
            if (self.cursor.row, self.cursor.column) > (0, 0):
                self.left()
                self.buffer.delete(self.cursor)
        else:
            self.buffer.insert(self.cursor, key)
            for _ in key:
                self.right()

    def keypress(self) -> None:
        key = self.screen.getkey()
        if key == "q": self._exit()
        elif key == "KEY_UP": self.up()
        elif key == "KEY_DOWN": self.down()
        elif key == "KEY_LEFT": self.left()
        elif key == "KEY_RIGHT": self.right()
        else: self.insert(key)

    def entry(self) -> None:
        while True:
            self.draw()
            self.keypress()

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    arguments = parser.parse_args()
    curses.wrapper(Oxygen, arguments.file)