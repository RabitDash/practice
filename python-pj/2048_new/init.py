from tools import State
import constants as c


class Init(State):

    def __init__(self):
        super(Init, self).__init__()
        self.score = 0
        self.highscore = 0
        self.field = None

    # 单例模式
    def __new__(cls, *more):
        if not cls.__instance:
            cls.__instance = super(Init, cls).__new__(cls)
        return cls.__instance

    def initScore(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.score = 0

    def initField(self):
        self.field = [[0 for i in range(c.width)] for j in range(c.height)]

    def startup(self):
        self.state = 'Init'
        self.previous = 'None'
        self.next = 'Run'

    def update(self):
        control = tools.Control()
        initialize = Init()

        initialize.initScore()
        initialize.initField()

        control.setScore(initialize.score)
        control.setHighScore(initialize.highscore)
        control.setField(initialize.field())
        control.switchState(initialize.next)
