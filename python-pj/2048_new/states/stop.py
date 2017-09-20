from ..tools import _State
from ..tools import Control as c

class stop(_State):

    def __init__(self):
        super(stop, self).__init__()

    def startup(self):
        self.state = 'Stop'
        self.previous = 'Init'
        self.next = 'None'

    def update(self):
        pass


