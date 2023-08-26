# should be initialized with a name as a string 
class Restaurant:
    def __init__(self, name = ''):
        self._name = name

    def given_name(self):
        return self._name