from Day6.Util import Util
from Day6.classes.Orbits import Orbits

util = Util()
values = util.parse("input.txt")
orbits = Orbits(values)

print("Checksum: ", orbits.checksum())
print(orbits.distance_between('YOU', 'SAN'))
