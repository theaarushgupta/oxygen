import curses
import sys
import argparse

from oxygen import file
from oxygen import window
from oxygen import cursor
from oxygen import color

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    arguments = parser.parse_args()
    buffer = file.load(arguments.file)
    def _main(screen: "curses._CursesWindow") -> None:
        cursor_ = cursor.Cursor(buffer)
        window_ = window.Window(buffer, cursor_, curses.LINES - 1, curses.COLS - 1)
        color_ = color.Color(screen)
        colorscheme = color_.create(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        color_.apply(colorscheme)
        while True:
            screen.erase()
            for row, line in enumerate(buffer[window_.row:window_.row + window_.rowCount]):
                screen.addstr(row, 0, line)
            screen.move(*window_.translate())
            key = screen.getkey()
            if key == "q":
                sys.exit(0)
            elif key == "KEY_UP":
                cursor_.up()
                window_.up()
            elif key == "KEY_DOWN":
                cursor_.down()
                window_.down()
            elif key == "KEY_LEFT":
                cursor_.left()
                window_.up()
            elif key == "KEY_RIGHT":
                cursor_.right()
                window_.down()
    curses.wrapper(_main)