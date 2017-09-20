    # -*- coding:utf-8 -*-

# 使用有限状态机的2048游戏

import curses
from constant import *
from collections import defaultdict



class Control(object):

    __instance = None

    def __init__(self):
        self.state_dict = {}
        self.state_name = None
        self.state = None
        self.done = False

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Control, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def setScore(self, score):
        self.score = score

    def setHighscore(self, highscore):
        self.highscore = highscore

    def getScore(self):
        return self.score

    def getHighscore(self):
        return self.highscore

    def setField(self, field):
        self.field = field

    def getField(self):
        return self.field

    def setup_states(self, state_dict, start_state):
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]


    def draw(self, screen):
        help_string1 = '(W)Up (S)Down (A)Left (D)Right'
        help_string2 = '      (R)Restart (Q)Exit'
        gameover_string = '               GAME OVER'
        win_string = '             YOU WIN!'

        def cast(string):
            screen.addstr(string + '\n')

        # 绘制水平分割线
        def drawSeparator():
            line = '+' + ('+------' * width + '+')[1:]
            separator = defaultdict(lambda: line)
            if not hasattr(drawSeparator, "counter"):
                drawSeparator.counter = 0
            cast(separator[drawSeparator.counter])
            drawSeparator.counter += 1

        # 绘制行以及数字
        def drawRow(row):
            cast(''.join('|{: ^5} '.format(num) if num > 0 else '|      ' for num in row) + '|')

        
        def drawScore(self):
            cast('SCORE: ' + str(self.score))   # 输出当前分数
            if 0 != self.highscore:             # 输出最高分
                cast('HIGHSCORE: ' + str(self.highscore))

        # 绘制矩阵
        def drawField(self):
            for row in self.field:
                drawSeparator()
                drawRow(row)
            drawSeparator()

        def drawHelp(self):
            cast(help_string1)
            cast(help_string2)

        # 绘制各种东西
        screen.clear()
        drawScore(self)
        drawField(self)
        drawHelp(self)


    def switchState(self):
        previous, self.state_name = self.state_name, self.state.next
        self.state = self.state_dict[self.state_name]
        self.state.previous = previous

    def update(self):
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.switchState()
        self.state.update()


    def action(char):
        return actions[char]

    def eventloop(self):
        pass

    # contains main loop
    def main(self):
        curses.use_default_colors()
        while not self.done:
            self.eventloop()
            self.update()

class _State(object):
    """Base class for all game states"""

    def __init__(self):
        self.done = False
        self.quit = False
        self.next = None
        self.previous = None
        self.game_data = {}

    def startup(self, game_data):
        self.game_data = game_data

    def cleanup(self):
        self.done = False
        return self.game_data

    def update(self):
        pass




# curses.wrapper(main)