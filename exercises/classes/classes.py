import datetime


class Book:

    def __init__(self):
        # Establish the properties of each book
        # with a default value
        self.title = ""
        self.publisher = ""
        self.author = ""
        self.current_page = 1
        self.year_published = 0
        self.currently_reading = False

    def start_reading(self):
        self.currently_reading = True
        print(f'You start reading {self.title} at page {self.current_page}')

    def stop_reading(self, page):
        self.current_page = page



mockingbird = Book()
mockingbird.title = "To Kill a Mockingbird"
mockingbird.publisher = "Penguin Books"
mockingbird.author = "Harper Lee"
mockingbird.year_published = 1960
mockingbird.publisher = "J. B. Lippincott & Co."

for prop, value in mockingbird.__dict__.items():
    print("book:",f'{prop}:\n{value}\n')


print(mockingbird.currently_reading)
mockingbird.start_reading()
print(mockingbird.currently_reading)
mockingbird.stop_reading(34)
mockingbird.start_reading()
mockingbird.stop_reading(89)
mockingbird.start_reading()



class Pizza:
    def __init__(self):
        self.size = 0
        self.type = ""
        self.toppings = []
        self.ordered = False

    def add_topping(self,toppings):
        self.toppings.append(toppings)

    def order_zah(self):
        sep = " and "
        self.ordered = True
        list_toppings = sep.join(self.toppings)
        print(f"You ordered a {self.size} inch {self.type} pizza, with {list_toppings}")

pepperoni = Pizza()
pepperoni.size = 73
pepperoni.type = "Meat"
pepperoni.add_topping("sausage")
pepperoni.add_topping("onion")
pepperoni.add_topping("olives")
pepperoni.order_zah()

for prop, value in pepperoni.__dict__.items():
    print("Pizza:",f'{prop}:\n{value}\n')

class Animal:
    def __init__(self, leg_num, species, owner="Happy Acres Breeding"):
        self.owner = owner
        self.species = species
        self.leg_num = leg_num

    def set_solid_food_date(self):
        self.set_solid_food_date = datetime.datetime.now().strftime("%x")

    def move(self, speed):
        return(f"{self.species} moves at {speed} meeters per second")

class Dog(Animal):
    def __init__(self, breed):
        self.breed = breed
        super().__init__(3, "dog")

collie = Dog("collie")
print(collie)
collie.set_solid_food_date()



class Vehicle:
    def __init__(self, main_color, maximum_occupancy):
        self.main_color = main_color
        self.maximum_occupancy = maximum_occupancy
    def drive(self):
        print("Vroooom!")


# Electric motorcycle
class Zero(Vehicle):
    def __init__(self):
        self.battery_kwh = 0

    def charge_battery(self):
        print("Battery Charged")
# Propellor light aircraft
class Cessna(Vehicle):
    def __init__(self):
        self.fuel_capacity = 0


    def refuel_tank(self):
        print("tank full")

# Gas powered truck
class Ram(Vehicle):
    def __init__(self, fuel_capacity):
        self.fuel_capacity = fuel_capacity
        super().__init__("Green", 45)

    def refuel_tank(self):
        print("tank full")

# Electric vehicle
class Tesla(Vehicle):
    def __init__(self, battery_kwh):
        self.battery_kwh = battery_kwh
        super().__init__("Blue", 2)
    def charge_battery(self):
        self.battery_kwh = 100
    def drive(self):
        print("Zoooooooooooom!")

vehicle = Tesla(100)
print(vehicle)
vehicle.drive()
vehicle = Ram(200)

fxs = Zero()
modelS = Tesla(100)
mx410 = Cessna()

fxs.drive()
modelS.drive()
mx410.drive()