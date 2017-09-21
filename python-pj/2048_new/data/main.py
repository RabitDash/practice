import curses

import constants as constants
from tools import tools

stdscr = curses.initscr()

def main(stdscr):
    curses.start_color()
    curses.use_default_colors()
    c = tools.Control()
    c.setScreen(stdscr)
    c.setStateDict(constants.state_dict)
    c.setState('Init')
    c.main()

main(stdscr)
