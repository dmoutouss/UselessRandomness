import random

class NamePart:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

class FirstName(NamePart):
    def __init__(self, value):
        super().__init__(value)

class LastName(NamePart):
    def __init__(self, value):
        super().__init__(value)

class NameGenerator:
    def __init__(self, first_names, last_names):
        self.first_names = [FirstName(name) for name in first_names]
        self.last_names = [LastName(name) for name in last_names]

    def generate_name(self):
        first_name = self.get_random_first_name()
        last_name = self.get_random_last_name()
        return f"{first_name.get_value()} {last_name.get_value()}"

    def get_random_first_name(self):
        return random.choice(self.first_names)

    def get_random_last_name(self):
        return random.choice(self.last_names)

first_names = ["James", "John", "Robert", "Michael", "William", "David", "Richard", "Joseph", "Thomas", "Charles",
               "Christopher", "Daniel", "Matthew", "Anthony", "Donald", "Mark", "Paul", "Steven", "Andrew", "Kenneth",
               "George", "Joshua", "Kevin", "Brian", "Edward", "Ronald", "Timothy", "Jason", "Jeffrey", "Ryan"]

last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor",
              "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson",
              "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "Hernandez", "King"]

def main():
    generator = NameGenerator(first_names, last_names)

    for _ in range(10):
        print(generator.generate_name())

if __name__ == "__main__":
    main()
