actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit', 'Tap']
directions = ['Up', 'Left', 'Down', 'Right']
letter_codes = [ord(ch) for ch in 'WASDRQTwasdrqt']
actions_dict = dict(zip(letter_codes, actions * 2))
