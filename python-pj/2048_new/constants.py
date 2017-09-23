letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']
actionsDict = dict(zip(letter_codes, actions * 2))


height = 4
width = 4
win_value = 32
