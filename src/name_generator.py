from .first_name import FirstName
from .last_name import LastName

class NameGenerator:
    def __init__(self):
        self.first_name = FirstName()
        self.last_name = LastName()

    def generate(self):
        return self.first_name.get_random() + ' ' + self.last_name.get_random()
