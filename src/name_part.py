class NamePart:
    def __init__(self, name_part_file):
        with open(name_part_file, 'r') as file:
            self.names = file.read().splitlines()

    def get_random(self):
        import random
        return random.choice(self.names)
