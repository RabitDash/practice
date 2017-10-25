from random import randrange, choice
from collections import defaultdict

import data.tools as tools

actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']


class Run(tools._State):

    def __init__(self):
        super(Run, self).__init__()
        self.need_event = False
        self.stop = False

    # 对角线翻转
    def transpose(self, field):
        return [list(row) for row in zip(*field)]

    # 垂直镜面翻转
    def invert(self, field):
        return [row[::-1] for row in field]

    # 判断是否能够移动
    def move_is_possible(self, direction):
        def row_is_left_movable(row):
            def change(i):
                if row[i] == 0 and row[i + 1] != 0:
                    return True
                if row[i] != 0 and row[i + 1] == row[i]:
                    return True
                return False

            return any(change(i) for i in range(len(row) - 1))

        check = {}
        check['Left'] = lambda field: any(row_is_left_movable(row) for row in field)

        check['Right'] = lambda field: check['Left'](self.invert(field))

        check['Up'] = lambda field: check['Left'](self.transpose(field))

        check['Down'] = lambda field: check['Right'](self.transpose(field))

        if direction in check:
            return check[direction](self.field)
        else:
            return False

    def move(self, direction):

        # 接受用户行为, 取得移动方向
        def move_row_left(row):

            # 移动后补空
            def tighten(row):
                new_row = [i for i in row if i != 0]
                new_row += [0 for i in range(len(row) - len(new_row))]
                return new_row

            # 合并相同数字
            def merge(row):
                pair = False
                new_row = []
                for i in range(len(row)):
                    if pair:
                        new_row.append(2 * row[i])
                        self.score += 2 * row[i]
                        pair = False
                    else:
                        if i + 1 < len(row) and row[i] == row[i + 1]:
                            pair = True
                            new_row.append(0)
                        else:
                            new_row.append(row[i])
                assert len(new_row) == len(row)
                return new_row

            return tighten(merge(tighten(row)))

        moves = {}

        moves['Left'] = lambda field: [move_row_left(row) for row in field]
        moves['Right'] = lambda field: self.invert(moves['Left'](self.invert(field)))
        moves['Up'] = lambda field: self.transpose(moves['Left'](self.transpose(field)))
        moves['Down'] = lambda field: self.transpose(moves['Right'](self.transpose(field)))

        # 测试各个方向是否可以移动
        if direction in moves:
            if self.move_is_possible(direction):
                self.field = moves[direction](self.field)
                self.spawn()
                self.need_event = False
                return True
            else:
                self.need_event = False
                return False

    def is_win(self):
        return any(any(i >= self.win_value for i in row) for row in self.field)

    def is_gameover(self):
        return not any(self.move_is_possible(move) for move in actions)

    def draw(self, screen):
        help_string1 = '(W)Up (S)Down (A)Left (D)Right'
        help_string2 = '      (R)Restart (Q)Exit'
        gameover_string = '           GAME OVER'
        win_string = '           YOU WIN!'

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
        new_element = 4 if randrange(100) > 89 else 2
        (i, j) = choice([(i, j) for i in range(self.width) for j in range(self.height) if self.field[i][j] == 0])
        self.field[i][j] = new_element

    def startup(self, game_data):
        self.next = 'Halt'
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
        self.move(direction = event)
        self.stop = self.draw(screen)
        if event is 'Restart':
            self.done = True
            self.next = 'Init'
        if not self.stop:
            self.need_event = True
        else:
            self.done = True
            
    def get_event(self, event):
        self.event = event

