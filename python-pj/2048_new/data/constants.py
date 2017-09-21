from states.init import Init
from states.run import Run
from states.stop import Stop


letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']
actionsDict = dict(zip(letter_codes, actions * 2))

state_dict = {
    'Init': Init,
    'Run': Run,
    'Stop': Stop
}

height = 4
width = 4
win_value = 32

