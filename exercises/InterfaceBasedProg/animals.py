from movements import Walking, Swimming, Flying
from habitat import Habitat


class Penguin(Walking, Swimming):
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f"{self.name} the Penguin waddles")


if __name__ == "__main__":

    # Create a penguin
    bob = Penguin("Bob")

    # Create a habitat
    SeaWorld = Habitat("Jerry")
    SeaWorld.add_animal(bob)

    print(SeaWorld.animals)

class PaintedDog(Walking):
    def __init__(self, name):
        self.name = name

if __name__ == "__main__":

    bob = Penguin("Bob")
    ralph = PaintedDog("Ralph")

    SeaWorld = Habitat("Terry")
    SeaWorld.add_animal(bob)
    SeaWorld.add_animal(ralph)

    print(SeaWorld.animals)