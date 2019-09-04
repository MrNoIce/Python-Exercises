class Boat:
    def __init__(self, type, propulsion):
        self.type = type
        self.propulsion = propulsion

    def move(self, speed):
        return f"The boat is moving at {speed} mph"

class Kayak(Boat):
    def __init__(self, passengers=1):
        super().__init__("kayak", "paddle")
        self.passengers = passengers

    def paddle(self):
        print(f'I like to go out in my Kayak. {self.move(13)}')




seaghost = Kayak(13)
seaghost.paddle()









# Define a class called Boat
# Give it a method that allows the boat to move that prints the speed it's moving
# Define a Class called Kayak
# Make it a derived class of Boat
# Give it a method called paddle that uses its inherited move method
# Make a Kayak instance and 'paddle' it
class Electric:
    def __init__(self):
        self.battery_capacity = 0
        self.battery_level = 0



class Gas:
    def __init__(self):
        self.fuel_capacity = 0
        self.fuel_level = 0


class Vehicle:
    def __init__(self, model, manufacturer, horsepower, wheel_count):
        self.model = model
        self.manufacturer = manufacturer
        self.horsepower = 0
        self.wheel_count = 0
    def drive(self, lowerby):
        self.gas_level -= lowerby
        print(f'Fuel tank level is {self.gas_level}')
    def refuel(self):
        self.fuel_capacity = self.fuel_capacity

class Mustang(Vehicle):
    def __init__(self):
        super().__init__("Mustang", "Ford", 20, 460, 4)

    def drive(self, lowerby):
        Vehicle.drive(4)
        print(f'Fuel tank level is {self.gas_level}')


class Ram(Vehicle):
    def __init__(self):
        Vehicle.__init__("Ram", "Dodge", 26, 395, 4)
        Gas.__init__(self, 26)

    def drive(self, lowerby):
        Vehicle.drive(6)
        print(f'Fuel tank level is {self.gas_level}')


class Leaf(Vehicle, Electric):
    def __init__(self):
        Vehicle.__init__(self,"Leaf", "Nissan", 50, 4)
        Electric.__init__(self)

    def drive(self, lowerby):
        Vehicle.drive(6)
        print(f'Fuel tank level is {self.gas_level}')








# Create a Nissan Leaf class
#     * `manufacturer` attribute
#     * `model` attribute
#     * `battery_capacity` attribute
#     * `battery_level` attribute
#     * `horsepower` attribute
#     * `wheel_count` attribute
#     * `drive()` method lowers `battery_level` by 2 each time it is invoked
#     * `recharge()` method sets `battery_level` to `battery_capacity` value


# Create a Ford Mustang class
#     * `manufacturer` attribute
#     * `model` attribute
#     * `fuel_capacity` attribute
#     * `gas_level` attribute
#     * `horsepower` attribute
#     * `wheel_count` attribute
#     * `drive()` method lowers `gas_level` by 4 each time it is invoked
#     * `refuel()` method method sets `gas_level` to `fuel_capacity` value

# Create a Dodge Ram class
#     * `manufacturer` attribute
#     * `model` attribute
#     * `fuel_capacity` attribute
#     * `gas_level` attribute
#     * `horsepower` attribute
#     * `wheel_count` attribute
#     * `drive()` method lowers `gas_level` by 4 each time it is invoked
#     * `refuel()` method method sets `gas_level` to `fuel_capacity` value