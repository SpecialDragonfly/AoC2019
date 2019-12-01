from Day1.Util import Util
from Day1.classes.SpaceModule import SpaceModule

util = Util()
values = util.parse("input.txt")
totalFuel = 0
for value in values:
    module = SpaceModule(value)
    totalFuel += module.fuel_needed()
print(totalFuel)
