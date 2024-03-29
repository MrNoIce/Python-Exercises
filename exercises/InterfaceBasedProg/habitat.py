

from movements import Swimming


class Habitat:

    def __init__(self, name):
        self.name = name
        self.animals = set()

    def add_animal(self, animal):
        self.animals.add(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)


class Aquarium(Habitat):

    def __init__(self):
        super().__init__()

    def add_animal(self, animal):
        # Add animal only if it inherited from
        # the Swimming interface class
        if isinstance(animal, Swimming):
            self.animals.add(animal)