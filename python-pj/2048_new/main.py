import curses
from tools import Control

stdscr = curses.initscr()

def main(stdscr):
    curses.use_default_colors()
    c = Control()
    c.setScreen(stdscr)
