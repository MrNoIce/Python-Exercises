class GasPowered:

    def __init__(self, capacity):
        self.fuel_capacity = capacity
        self.gas_level = 0

    def drive(self, lowerby):
        self.gas_level -= lowerby
        print(f'You have {self.gas_level} gallons left, you road hog')

    def refuel(self):
        self.gas_level = self.fuel_capacity
