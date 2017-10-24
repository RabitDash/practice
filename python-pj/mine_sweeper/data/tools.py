import curses
from .constants import *
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
curses.start_color()
curses.use_default_colors()
stdscr.keypad(1)


# 获取用户输入
def get_user_action(keyboard):
    char = 'N'
    while char not in actions_dict:
        try:
            char = keyboard.getch()
        except KeyboardInterrupt:
            curses.endwin()
            curses.nocbreak()
            stdscr.keypad(0)
            curses.echo()
            curses.endwin()
            exit(0)

    return actions_dict[char]


class Control(object):
    """
    Control class for entire project.  Contains the game loop, and contains
    the event_loop which passes events to States as needed.  Logic for flipping
    states is also found here.
    """
    def __init__(self):
        self.screen = stdscr
        self.done = False
        self.state_dict = {}
        self.state_name = None
        self.state = None
        self.game_data = {}
        self.event = 'None'

    def setup_states(self, state_dict, start_state):
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]

    def update(self):
        self.state.update(self.screen, self.event)

        if self.state.quit:  # 如果state给出退出信号
            self.done = True
        elif self.state.done:  # 如果state结束
            self.flip_state()

    def flip_state(self):
        previous, self.state_name = self.state_name, self.state.next
        persist = self.state.cleanup()

        self.state = self.state_dict[self.state_name]  # 转换状态
        self.state.previous = previous
        self.state.startup(persist)

    def event_loop(self):
        if self.state.need_event:
            self.event = get_user_action(stdscr)
        else:
            self.state.get_event(self.event)

    def main(self):
        """Main loop for entire program"""

        while not self.done:
            self.event_loop()
            try:
                self.update()
            except KeyboardInterrupt:
                curses.endwin()
                curses.nocbreak()
                stdscr.keypad(0)
                curses.echo()
                curses.endwin()
                exit(0)
        curses.endwin()


class _State(object):
    """Base class for all game states"""
    def __init__(self):
        self.done = False
        self.quit = False
        self.next = None
        self.previous = None
        self.game_data = {}

    def get_event(self, event):
        pass

    def startup(self, game_data):
        self.game_data = game_data

    def cleanup(self):
        self.done = False
        return self.game_data

    def update(self, screen, event):
        pass


def create_game_data_dict():
    """Create a dictionary of persistant values the player
    carries between states"""

    data_dict = {'highscore': 0,
                 'score': 0,
                 'width': 4,
                 'height': 4,
                 'mines': 4,
    }

    return data_dict




