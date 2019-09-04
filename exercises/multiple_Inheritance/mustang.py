from vehicle import Vehicle
from GasPowered import GasPowered

class Mustang(Vehicle, GasPowered):

    def __init__(self):
        Vehicle.__init__(self, "Mustang", "Ford", 460, 4)
        GasPowered.__init__(self, 20)

    def drive(self):
        GasPowered.drive(self, 4)