from vehicle import Vehicle
from ElectricPowered import ElectricPowered


class Leaf(Vehicle, ElectricPowered):

    def __init__(self):
        Vehicle.__init__(self, "Leaf", "Nissan", 50, 4)
        ElectricPowered.__init__(self, 45)

    def drive(self):
        ElectricPowered.drive(self, 1)