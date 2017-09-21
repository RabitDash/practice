from random import randrange, choice

from constants import *
from ..tools import *

class Run(tools.State):

    def __init__(self):
       # super(Run, self).__init__()
        pass
    # 单例模式
    def __new__(cls, *more):
        if not cls.__instance:
            cls.__instance = super(Run, cls).__new__(cls)

        return cls.__instance
    def setScore(self, score):
        self.score = score

    def setField(self, field):
        self.field = field

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
        '''
        接受用户行为, 取得移动方向
        :param direction: 
        :return: 
        '''

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

        # moves方法字典
        def moves(self):
            moves = {}

            moves['Left'] = lambda field: [move_row_left(row) for row in field]
            moves['Right'] = lambda field: self.invert(moves['Left'](self.invert(field)))
            moves['Up'] = lambda field: self.transpose(moves['Left'](self.transpose(field)))
            moves['Down'] = lambda field: self.transpose(moves['Right'](self.transpose(field)))

            return moves

        # 随机生成
        def spawn(self):
            new_element = 4 if randrange(100) > 89 else 2
            (i, j) = choice([(i, j) for i in range(width) for j in range(height) if self.field[i][j] == 0])
            self.field[i][j] = new_element

        # 测试各个方向是否可以移动
        if direction in moves:
            if self.move_is_possible(direction):
                self.field = moves(self)[direction](self.field)
                spawn(self)
                return True
            else:
                return False


    def is_win(self):
        return any(any(i >= win_value for i in row) for row in self.field)

    def is_gameover(self):
        return not any(self.move_is_possible(move) for move in actions)


    def startup(self):
        self.state = 'Run'
        self.next = 'Stop'
        self.previous = 'Init'

    def update(self):
        control = tools.Control()
        run = Run()
        action = control.getAction()
        while not self.is_win() and self.is_gameover():
            run.setScore(control.getScore())
            run.setField(control.getField())
            run.move(action)
            control.setScore(run.score)
            control.setField(run.field)
            control.draw()
        if self.is_win():
            control.draw('You Win!')
        elif self.is_gameover():
            control.draw('Fuck')
        control.switchState(('Stop'))