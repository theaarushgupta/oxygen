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

    def entry(self) -> None:
        while True:
            self.screen.erase()
            for row, line in enumerate(self.buffer[self.window.row:self.window.row + self.window.rowCount]):
                if row == self.cursor.row - self.window.row and self.window.column > 0:
                    line = "«" + line[self.window.column + 1:]
                if len(line) > self.window.columnCount:
                    line = line[:self.window.columnCount - 1] + "»"
                self.screen.addstr(row, 0, line)
            self.screen.move(*self.window.translate())
            key = self.screen.getkey()
            if key == "q":
                sys.exit(0)
            elif key == "KEY_UP":
                self.cursor.up()
                self.window.up()
                self.window.horizontalScroll()
            elif key == "KEY_DOWN":
                self.cursor.down()
                self.window.down()
                self.window.horizontalScroll()
            elif key == "KEY_LEFT":
                self.cursor.left()
                self.window.up()
                self.window.horizontalScroll()
            elif key == "KEY_RIGHT":
                    self.cursor.right()
                    self.window.down()
                    self.window.horizontalScroll()
            else:
                self.buffer.insert(self.cursor, key)
                for _ in key:
                    self.cursor.right()
                    self.window.down()
                    self.window.horizontalScroll()

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    arguments = parser.parse_args()
    curses.wrapper(Oxygen, arguments.file)