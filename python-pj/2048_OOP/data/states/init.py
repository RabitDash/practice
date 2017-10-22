import data.tools as tools


class Init(tools._State):
    def __init__(self):
        super(Init, self).__init__()
        self.name = 'Init'
        self.width = 4
        self.height = 4
        self.field = []
        self.need_event = False

    def startup(self, game_data):
        self.next = 'Run'
        self.previous = 'None'

        if self.game_data['score'] > self.game_data['highscore']:
            self.game_data['highscore'] = self.game_data['score']

        self.game_data['score'] = 0

    def cleanup(self):
        self.done = False
        return self.game_data

    def update(self, screen, event):
        self.next = 'Run'
        self.previous = 'Init'

        if not self.game_data :
            self.game_data = tools.create_game_data_dict()
        if self.game_data['score'] > self.game_data['highscore']:
            self.game_data['highscore'] = self.game_data['score']
        self.done = True

    def get_event(self, event):
        self.event = event
