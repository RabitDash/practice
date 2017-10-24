import data.tools as tools

class Init(tools._State):
    def __init__(self):
        super(Init, self).__init__()
        self.name = 'Init'
        self.field = []
        self.need_event = False
        self.next = 'Run'
        self.previous = 'Init'

    def startup(self, game_data):
        if self.game_data['score'] > self.game_data['highscore']:
            self.game_data['highscore'] = self.game_data['score']

        self.game_data['score'] = 0

    def cleanup(self):
        self.done = False
        return self.game_data

    def update(self, screen, event):
        if not self.game_data:
            self.game_data = tools.create_game_data_dict()
        if self.game_data['score'] > self.game_data['highscore']:
            self.game_data['highscore'] = self.game_data['score']
        self.done = True

    def get_event(self, event):
        pass
