from functools import reduce

from Day3.Util import Util
from Day3.classes.Wire import Wire

util = Util()
values = util.parse('input.txt')
initial_wire = Wire()
initial_wire.trace(values[0])
print(len(set(initial_wire.Locations)))
second_wire = Wire()
second_wire.trace(values[1])
print(len(set(second_wire.Locations)))
print("Intersecting")
intersection = set(second_wire.Locations).union(set(initial_wire.Locations))
print(len(intersection))

