from vehicle import Vehicle
from GasPowered import GasPowered


class Ram(Vehicle, GasPowered):

    def __init__(self):
        Vehicle.__init__(self, "Ram", "Dodge", 395, 4)
        GasPowered.__init__(self, 26)

    def drive(self):
        GasPowered.drive(self, 6)