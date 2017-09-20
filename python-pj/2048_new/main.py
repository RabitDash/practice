import curses
from tools import Control
from constant import *

stdscr = curses.initscr()

def main(stdscr):
    curses.use_default_colors()
    c = Control()
    c.setScreen(stdscr)
    c.state_dict = state_dict
