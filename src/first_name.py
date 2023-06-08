from .name_part import NamePart

class FirstName(NamePart):
    def __init__(self):
        super().__init__('first_names.txt')
