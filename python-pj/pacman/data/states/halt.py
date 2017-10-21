import data.tools as tools


class Halt(tools._State):

    def __init__(self):
        super(Halt, self).__init__()
        self.need_event = False

    def startup(self, game_data):
        self.need_event = True

    def cleanup(self):
        pass

    def update(self, screen, event):
        if event is 'Restart':
            self.next = 'Init'
            self.done = True
        elif event is 'Quit':
            self.quit = True
            self.done = True
        else:
            self.next = 'Halt'
            self.done = True
        self.need_event = False

    def get_event(self, event):
        self.event = event