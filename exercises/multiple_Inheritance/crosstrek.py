from vehicle import Vehicle
from ElectricPowered import ElectricPowered
from GasPowered import GasPowered


class CrossTrek(Vehicle, ElectricPowered, GasPowered):

    def __init__(self):
        Vehicle.__init__(self, "Crosstrek", "Subaru", 60, 4)
        ElectricPowered.__init__(self, 40)
        GasPowered.__init__(self, 6)

    def refuel(self):
        ElectricPowered.refuel(self)
        GasPowered.refuel(self)

    def drive(self):
        ElectricPowered.drive(self, 2)
        GasPowered.drive(self, 0.5)