from ..tools import _State,Control
from ..constant import *

class Init(_State):

    def __init__(self):
        super(Init, self).__init__()
        self.score = 0
        self.highscore = 0
        self.field = None


    def initScore(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.score = 0

    def initField(self):
        self.field = [[0 for i in range(width)] for j in range(height)]
        return self.field

    def startup(self, keys):
        self.state = 'Init'
        self.next = 'Run'

control = Control()
init = Init()
control.setScore(init.score)
control.setHighScore(init.highscore)
control.setField(init.initField())


