import collections


class ImmutableDict(collections.UserDict):
    def __init__(self, *args, **kwargs):
        super(ImmutableDict, self).__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        if key in self.keys():
            raise TypeError('Fuck!')
        else:
            self.data[key] = value

    def __delitem__(self, key):
        if key in self.keys():
            raise TypeError('Fuck!')
        else:
            raise KeyError
