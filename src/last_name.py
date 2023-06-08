from .name_part import NamePart

class LastName(NamePart):
    def __init__(self):
        super().__init__('last_names.txt')
