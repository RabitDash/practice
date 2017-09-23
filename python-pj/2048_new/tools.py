# -*- coding:utf-8 -*-
# 使用有限状态机的2048游戏

from collections import defaultdict
from init import Init
from run import Run
from stop import Stop

letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']
actionsDict = dict(zip(letter_codes, actions * 2))

state_dict = {
    'Init': Init(),
    'Run': Run(),
    'Stop': Stop(),
}

height = 4
width = 4
win_value = 2048


class Control(object):

    __instance = None

    def __init__(self):
        self.state_dict = {}
        self.state_name = None
        self.state = None
        self.done = False

    def __new__(cls, *more):
        if not cls.__instance:
            cls.__instance = super(Control, cls).__new__(cls)
        return cls.__instance

    def setScore(self, score):
        self.score = score

    def setHighscore(self, highscore):
        self.highscore = highscore

    def setScreen(self, screen):
        self.screen = screen

    def setField(self, field):
        self.field = field

    def setStateDict(self, state_dict):
        self.state_dict = state_dict

    def setState(self, state):
        self.state = state_dict[state]

    def getScore(self):
        return self.score

    def getHighscore(self):
        return self.highscore

    def getScreen(self):
        return self.screen

    def getField(self):
        return self.field

    def getStates(self):
        return self.state_dict

    def draw(self, string=''):
        help_string1 = '(W)Up (S)Down (A)Left (D)Right'
        help_string2 = '      (R)Restart (Q)Exit'

        def cast(string):
            if string is not '':
                self.screen.addstr(string + '\n')

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
        self.screen.clear()
        drawScore(self)
        drawField(self)
        drawHelp(self)
        cast(string)

    def getAction(self):
        char = 'N'
        while char not in actionsDict:
            char = self.screen.getch()
        return actionsDict[char]    # 获取输入并返回对应行为

    def switchState(self, next):
        self.state = state_dict[next]

    def main(self):
        control = Control()
        control.setState('Init')
        while self.done == False:
            self.state.update()


class State(object):
    """Base class for all game states"""

    def __init__(self):
        self.done = False
        self.quit = False
        self.next = None
        self.previous = None

    def startup(self):
        pass

    def update(self):
        pass




# curses.wrapper(main)
