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
    buffer_ = file.load(arguments.file)
    def _main(screen: "curses._CursesWindow") -> None:
        cursor_ = cursor.Cursor(buffer_)
        window_ = window.Window(buffer_, cursor_, curses.LINES - 1, curses.COLS - 1)
        color_ = color.Color(screen)
        colorscheme = color_.create(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        color_.apply(colorscheme)
        def right() -> None:
            cursor_.right()
            window_.down()
            window_.horizontalScroll()
        while True:
            screen.erase()
            for row, line in enumerate(buffer_[window_.row:window_.row + window_.rowCount]):
                if row == cursor_.row - window_.row and window_.column > 0:
                    line = "«" + line[window_.column + 1:]
                if len(line) > window_.columnCount:
                    line = line[:window_.columnCount - 1] + "»"
                screen.addstr(row, 0, line)
            screen.move(*window_.translate())
            key = screen.getkey()
            if key == "q":
                sys.exit(0)
            elif key == "KEY_UP":
                cursor_.up()
                window_.up()
                window_.horizontalScroll()
            elif key == "KEY_DOWN":
                cursor_.down()
                window_.down()
                window_.horizontalScroll()
            elif key == "KEY_LEFT":
                cursor_.left()
                window_.up()
                window_.horizontalScroll()
            elif key == "KEY_RIGHT":
                right()
            else:
                buffer_.insert(cursor_, key)
                for _ in key:
                    right()
    curses.wrapper(_main)