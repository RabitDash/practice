import curses
from tools import Control

stdscr = curses.initscr()

def main(stdscr):
    curses.use_default_colors()
    c = Control()
    c.setScreen(stdscr)
    c.setup_states(state_dict = {
    'Init':init(),
    'Lose':pass,
    'Win':pass,
    'Run':run(),
    }, 'Init')
