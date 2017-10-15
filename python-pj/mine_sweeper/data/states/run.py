from random import randrange, choice
from collections import defaultdict

import data.tools as tools

actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']


class Run(tools._State):

    def __init__(self):
        super(Run, self).__init__()
        self.need_event = False
        self.stop = False

        # 随机生成
    def spawn(self):
        pass
        
    def is_win(self):
        pass

    def is_gameover(self):
        pass

    def draw(self, screen):
        help_string1 = '(W)Up (S)Down (A)Left (D)Right'
        help_string2 = '      (R)Restart (Q)Exit'
        gameover_string = '           GAME OVER'
        win_string = '           YOU WIN!'

        def cast(string):
            screen.addstr(string + '\n')

        def draw_hor_separator():
            pass

        def draw_row(row):
            pass
        screen.clear()
        cast('SCORE: ' + str(self.score))

        if 0 != self.highscore:
            cast('HIGHSCORE: ' + str(self.highscore))

        for row in self.field:# Draw something

        draw_hor_separator()

        if self.is_win():
            cast(win_string)
            cast(help_string2)
            return True
        else:
            if self.is_gameover():
                cast(gameover_string)
                cast(help_string2)
                return True
            else:
                cast(help_string1)

        cast(help_string2)

    def spawn(self):
        new_element = 0 if randrange(100) > 89 else 1
        (i, j) = choice([(i, j) for i in range(self.width) for j in range(self.height) if self.field[i][j] == 0])
        self.field[i][j] = new_element

    def startup(self, game_data):
        self.state = 'Run'
        self.next = None
        self.previous = 'Init'
        self.score = game_data['score']
        self.highscore = game_data['highscore']
        self.win_value = game_data['win_score']
        self.width = game_data['width']
        self.height = game_data['height']
        self.game_data = game_data
        self.field = [[0 for i in range(self.width)] for j in range(self.height)]
        self.spawn()

    def cleanup(self):
        self.done = False
        return self.game_data

    def update(self, screen, event):
        self.move(direction=event)
        self.stop = self.draw(screen)
        if not self.stop:
            self.need_event = True
            if event is 'Restart':
                self.next = 'Init'
                self.done = True
        else:
            self.next = 'Halt'
            self.done = True
            
    def get_event(self, event):
        self.event = event

