import curses

def main(stdscr):
    curses.use_default_colors()
    state_dict = {
        'Init': init,
        'Win': lambda: not_game('Win'),
        'Gameover': lambda: not_game('Gameover'),
        'Game': game
    }
    state = 'Init'
