from tools import tools

class Stop(tools.State):

    def __init__(self):
        pass
    # 单例模式
    def __new__(cls, *more):
        if not cls.__instance:
            cls.__instance = super(Stop, cls).__new__(cls)
        return cls.__instance

    def startup(self):
        self.state = 'Stop'
        self.previous = 'Init'
        self.next = 'None'

    def update(self):
        control = tools.Control()
        action = control.getAction()
        if action == 'Restart':
            control.switchState('Init')
        elif action == 'Quit':
            control.done = True

