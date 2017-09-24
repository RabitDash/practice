from random import randrange, choice
import data.tools as tools
from collections import defaultdict

class Init(tools._State):
    def __init__(self):
        super(Init, self).__init__()
        self.name = 'Init'
        self.width = 4
        self.height = 4
        self.field = []

    def startup(self, game_data):
        self.state = 'Init'
        if self.game_data is None:
            self.game_data = tools.create_game_data_dict()
        else:
            self.game_data = game_data
            if self.game_data['score'] > self.game_data['highscore']:
                self.game_data['highscore'] = self.game_data['score']
            self.game_data['score'] = 0
        self.score = game_data['score']
        self.highscore = game_data['highscore']

    def cleanup(self):
        self.done = False
        return self.game_data

    def update(self, screen, event):
        # self.done = True
        screen.addstr(str(event))

    def get_event(self, event):
        self.event = event
