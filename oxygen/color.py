import curses

class Color:
    def __init__(self, screen: "curses._CursesWindow") -> None:
        self.screen = screen

    def create(
        self,
        id_: int = 1,
        foreground: int = curses.COLOR_WHITE,
        background: int = curses.COLOR_BLACK
    ) -> int:
        curses.init_pair(id_, foreground, background)
        return curses.color_pair(id_)

    def apply(
        self,
        pair: int
    ) -> int:
        self.screen.bkgd(" ", pair)
