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
        self.next = 'Run'
        self.previous = 'None'

        if self.game_data['score'] > self.game_data['highscore']:
            self.game_data['highscore'] = self.game_data['score']

        self.game_data['score'] = 0

    def cleanup(self):
        self.done = False
        return self.game_data

    def update(self, screen, event):
        self.state = 'Init'
        self.next = 'Run'
        self.previous = 'None'

        if not self.game_data :
            self.game_data = tools.create_game_data_dict()
        if self.game_data['score'] > self.game_data['highscore']:
            self.game_data['highscore'] = self.game_data['score']
        if event == 'Restart':
            self.done = True

    def get_event(self, event):
        self.event = event
