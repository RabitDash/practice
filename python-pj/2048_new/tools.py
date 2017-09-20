    # -*- coding:utf-8 -*-

# 使用有限状态机的2048游戏

import curses
from constant import *
from collections import defaultdict



class Control(object):
    def __init__(self):
        self.state_dict = {}
        self.state_name = None
        self.state = None
        self.done = False




    def setup_states(self, state_dict, start_state):
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]

    def is_win(self):
        return any(any(i >= self.win_value for i in row) for row in self.field)

    def is_gameover(self):
        return not any(self.move_is_possible(move) for move in actions)

    def draw(self, screen):
        help_string1 = '(W)Up (S)Down (A)Left (D)Right'
        help_string2 = '      (R)Restart (Q)Exit'
        gameover_string = '               GAME OVER'
        win_string = '             YOU WIN!'

        def cast(string):
            screen.addstr(string + '\n')

        # 绘制水平分割线
        def draw_hor_separator():
            line = '+' + ('+------' * width + '+')[1:]
            separator = defaultdict(lambda: line)
            if not hasattr(draw_hor_separator, "counter"):
                draw_hor_separator.counter = 0
            cast(separator[draw_hor_separator.counter])
            draw_hor_separator.counter += 1

        # 绘制行以及数字
        def draw_row(row):
            cast(''.join('|{: ^5} '.format(num) if num > 0 else '|      ' for num in row) + '|')

        # 清屏并输出
        screen.clear()
        cast('SCORE: ' + str(self.score))

        if 0 != self.highscore:
            cast('HIGHSCORE: ' + str(self.highscore))

        for row in self.field:
            draw_hor_separator()
            draw_row(row)
        draw_hor_separator()


    def switchState(self):
        previous, self.state_name = self.state_name, self.state.next
        self.state = self.state_dict[self.state_name]
        self.state.previous = previous

    def update(self):
        self.current_time = pg.time.get_ticks()
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.switchState()
        self.state.update()

    def move_is_possible(self, direction):
        def row_is_left_movable(row):
            def change(i):
                if row[i] == 0 and row[i + 1] != 0:
                    return True
                if row[i] != 0 and row[i + 1] == row[i]:
                    return True
                return False

            return any(change(i) for i in range(len(row) - 1))

        # check方法字典
        def check():
            check = {}
            check['Left'] = lambda field: any(row_is_left_movable(row) for row in field)

            check['Right'] = lambda field: check['Left'](invert(field))

            check['Up'] = lambda field: check['Left'](transpose(field))

            check['Down'] = lambda field: check['Right'](transpose(field))
            return check


        if direction in check():
            return check[direction](self.field)
        else:
            return False

    def get_user_action(keyboard):
        char = 'N'
        while char not in actions_dict:
            char = keyboard.getch()
        return actions_dict[char]

    # contains main loop
    def main(self,stdscr):
        curses.use_default_colors()

        pass

class _State(object):
    """Base class for all game states"""

    def __init__(self):
        self.done = False
        self.quit = False
        self.next = None
        self.previous = None

    def startup(self):
        pass

    def update(self, keys):
        pass


def main(stdscr):
    # 有限状态机
    def init():

        game_field.reset()
        return 'Game'

    def not_game(state):

        game_field.draw(stdscr)
        action = get_user_action(stdscr)
        responses = defaultdict(lambda: state)
        responses['Restart'], responses['Exit'] = 'Init', 'Exit'
        return responses[action]

    def game():

        game_field.draw(stdscr)
        action = get_user_action(stdscr)

        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'
        if game_field.move(action):
            if game_field.is_win():
                return 'Win'
            if game_field.is_gameover():
                return 'Gameover'
        return 'Game'

    # 定义状态
    state_actions = {
        'Init': init,
        'Win': lambda: not_game('Win'),
        'Gameover': lambda: not_game('Gameover'),
        'Game': game
    }


    # 定义初始状态
    state = 'Init'

    # 主循环
    while state != 'Exit':
        state = state_actions[state]()


# 执行
curses.wrapper(main)