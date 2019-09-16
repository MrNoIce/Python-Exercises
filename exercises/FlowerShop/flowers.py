class Arrangement:

    def __init__(self):
        self.__flowers = []

    def enhance(self, flower):
        self.__flowers.append(flower)


class MothersDay(Arrangement):

    def __init__(self):
        super().__init__()
    def enhance(self, flower):
        try:
            if flower.needs_refrigeration == True:
                self.__flowers.append(flower)
        except AttributeError as ex:
            print("Fuck")

    # Actual typing check
    # Override the `enhance` method to ensure only
    # roses, lillies, and alstroemeria can be added


class ValentinesDay(Arrangement):
    def __init__(self):
        super().__init__()

class Organic:
    def __init__(self):
        self.needs_refrigeration = False
        self.stem_length = '4 in'
    def shipping(self):
        print("This item has shipped in a non-refrigerated container!")

class Not_Organic:
    def __init__(self):
        self.needs_refrigeration = True
        self.stem_length = '7 in'
    def shipping(self):
        print("This item has shipped in a refrigerated container!")



class Rose(Not_Organic):
    def __init__(self, color):
        Not_Organic.__init__(self)
        self.color = color

class Alstroemeria(Not_Organic):
    def __init__(self):
        Not_Organic.__init__(self)
        self.name = "Alstroemeria"

class Lillies(Not_Organic):
    def __init__(self):
        Not_Organic.__init__(self)
        self.name = "lillie"

class Dasies(Organic):
    def __init__(self):
        Organic.__init__(self)
        self.name = "dasey"
class Poppies(Organic):
    def __init__(self):
        Organic.__init__(self)
        self.name = "poppy"

class Babies_Breath(Organic):
    def __init__(self):
        Organic.__init__(self)
        self.name = "babies breath"

# if __name__ == "__main__":
#     for_beth = ValentinesDay()
#     red_rose = Rose()

daisey = Dasies()
mother = MothersDay()
rose1 = Rose("blue")
arr = Arrangement()
print(arr)
print(rose1)
print(mother)


