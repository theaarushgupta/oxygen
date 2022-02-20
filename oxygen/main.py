import curses
import sys
import argparse

from oxygen import file
from oxygen import window
from oxygen import cursor

from typing import Any

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    arguments = parser.parse_args()
    buffer = file.load(arguments.file)
    def _main(screen: Any) -> None:
        window_ = window.Window(curses.LINES - 1, curses.COLS - 1)
        cursor_ = cursor.Cursor(buffer)
        while True:
            screen.erase()
            for x, y in enumerate(buffer[:window_.rows]):
                screen.addstr(x, 0, y[:window_.columns])
            screen.move(cursor_.row, cursor_.column)
            key = screen.getkey()
            if key == "q":
                sys.exit(0)
            elif key == "KEY_UP":
                cursor_.up()
            elif key == "KEY_DOWN":
                cursor_.down()
            elif key == "KEY_LEFT":
                cursor_.left()
            elif key == "KEY_RIGHT":
                cursor_.right()
    curses.wrapper(_main)