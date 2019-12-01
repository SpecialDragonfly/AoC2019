import math


class SpaceModule:
    Mass = 0

    def __init__(self, mass):
        self.Mass = mass

    def fuel_needed(self):
        fuel_from_mass = math.floor(self.Mass / 3) - 2
        return fuel_from_mass + self.fuel_for_fuel(fuel_from_mass)

    def fuel_for_fuel(self, start):
        fuel = math.floor(start / 3) - 2
        if (fuel > 0):
            fuel += self.fuel_for_fuel(fuel)
        else:
            fuel = 0
        return fuel
