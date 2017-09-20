from ..tools import _State,Control
from ..constant import *

class Init(_State):

    def __init__(self):
        super(_State, self).__init__()
        self.score = 0
        self.highscore = 0
        self.field = None

    # 单例模式

    def init(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.score = 0
        self.field = [[0 for i in range(width)] for j in range(height)]
        return self.field

