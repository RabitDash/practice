from random import choice

import data.tools as tools
from ..constants import *


class Run(tools._State):

    def __init__(self):
        super(Run, self).__init__()
        self.need_event = False
        self.stop = False
        # 随机生成

        '''
        0 代表没地雷, 1 代表有地雷
        '''

    def spawn(self):
        new_element = 1
        for fuck in range(self.mines):
            (i, j) = choice([(i, j) for i in range(self.width) for j in range(self.height) if self.field[i][j] == 0])
            self.field[i][j] = new_element

    def is_win(self):
        if self.left_mines is 0:
            return True
        else:
            return False

        # 返回当前位置

    def is_hit(self):
        (x, y) = self.location
        if self.field[x][y] is 0:
            return False
        elif self.field[x][y] is 1:
            return True

    def move(self, event):
        (x, y) = self.location

        def in_border(location):
            (a, b) = location
            if a in range(self.width) and b in range(self.height):
                return True
            else:
                return False

        if event in directions:
            if event is 'Up':
                next_location = (x - 1, y)
                if in_border(next_location):
                    self.location = next_location
            elif event is 'Down':
                next_location = (x + 1, y)
                if in_border(next_location):
                    self.location = next_location
            elif event is 'Left':
                next_location = (x, y - 1)
                if in_border(next_location):
                    self.location = next_location
            elif event is 'Right':
                next_location = (x, y + 1)
                if in_border(next_location):
                    self.location = next_location

        if event is 'Tap':
            if self.is_hit():
                self.hit = True
            else:
                self.hit = False

    def draw(self, screen, fuck=''):
        help_string1 = '(W)Up (S)Down (A)Left (D)Right (T)Tap'
        help_string2 = '    (R)Restart (Q)Exit'
        gameover_string = '           GAME OVER'
        win_string = '           YOU WIN!'

        def cast(string):
            screen.addstr(string + '\n')
        screen.clear()

        if fuck is '':

            def draw_hor_separator():
                cast('+' + '-' * 9 + '+')

            def draw_row(row):
                cast('|' + ''.join('{:2}'.format(num) for num in row) + ' |')


            cast('SCORE: ' + str(self.score))
            if 0 != self.highscore:
                cast('HIGHSCORE: ' + str(self.highscore))

            draw_hor_separator()
            for row in self.field:
                draw_row(row)
            draw_hor_separator()
            cast('{}'.format(self.location))

            if self.is_win():
                cast(win_string)
                cast(help_string2)
                return True
            elif self.hit:
                cast(gameover_string)
                cast(help_string2)
                return True
            else:
                cast(help_string1)
            cast(help_string2)
            return False
        else:
            cast(fuck)

    def startup(self, game_data):
        self.score = game_data['score']
        self.highscore = game_data['highscore']
        self.width = game_data['width']
        self.height = game_data['height']
        self.mines = game_data['mines']
        self.left_mines = self.mines  # 还剩多少地雷
        self.hit = False  # 踩雷
        self.location = (0, 0)
        self.game_data = game_data
        self.field = [[0 for i in range(self.width)] for j in range(self.height)]
        self.spawn()
        self.need_event = True
        self.next = 'Halt'

    def cleanup(self):
        self.done = False
        self.need_event = False
        return self.game_data

    def update(self, screen, event):
        self.move(event)
        self.draw(screen)
        self.stop = self.draw(screen) or self.hit
        if event is 'Restart':
            self.done = True
            screen.clear()
            screen.addstr("Press W to continue")
            self.next = 'Init'

        if not self.stop:
            self.need_event = True
        else:
            self.done = True

        if event is 'Exit':
            self.quit = True

    def get_event(self, event):
        self.event = event
