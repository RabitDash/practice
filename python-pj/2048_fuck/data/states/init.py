from random import randrange, choice
import data.tools as tools
from collections import defaultdict

class Init(tools._State):
    def __init__(self):
        super(Init, self).__init__()
        self.name = 'Init'
        self.width = 4
        self.height = 4
        self.field = []

    def startup(self, game_data):
        self.state = 'Init'
        if self.game_data is None:
            self.game_data = tools.create_game_data_dict()
        else:
            self.game_data = game_data
            if game_data['Score'] > game_data['Highscore']:
                game_data['Highscore'] = game_data['Score']
            game_data['Score'] = 0
        self.score = game_data['Score']
        self.highscore = game_data['Highscore']
        self.spawn()

    def update(self, screen, event):
        # self.done = True
        screen.addstr(str(event))


    def draw(self, screen):
        help_string1 = '(W)Up (S)Down (A)Left (D)Right'
        help_string2 = '      (R)Restart (Q)Exit'

        def cast(string):
            screen.addstr(string + '\n')

        def draw_hor_separator():
            line = '+' + ('+------' * self.width + '+')[1:]
            separator = defaultdict(lambda: line)
            if not hasattr(draw_hor_separator, "counter"):
                draw_hor_separator.counter = 0
            cast(separator[draw_hor_separator.counter])
            draw_hor_separator.counter += 1

        def draw_row(row):
            cast(''.join('|{: ^5} '.format(num) if num > 0 else '|      ' for num in row) + '|')

        screen.clear()
        cast('SCORE: ' + str(self.score))

        if 0 != self.highscore:
            cast('HIGHSCORE: ' + str(self.highscore))

        for row in self.field:
            draw_hor_separator()
            draw_row(row)

        draw_hor_separator()

    def get_event(self, event):
        self.event = event
