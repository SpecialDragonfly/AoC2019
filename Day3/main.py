from functools import reduce

from Day3.Util import Util
from Day3.classes.Wire import Wire

x = ["a", "b", "c"]
y = ["c", "d", "e"]
print(x)
print(y)
print(set(x).intersection(set(y)))

util = Util()
values = util.parse('input.txt')
print(values[0])
print(values[1])
initial_wire = Wire()
initial_wire.trace(values[0])
second_wire = Wire()
second_wire.trace(values[1])
#initial_wire.intersect(second_wire)
print(initial_wire.Locations[0].to_string())
print(initial_wire.Locations[1].to_string())
print(initial_wire.Locations[2].to_string())

print(second_wire.Locations[0].to_string())
print(second_wire.Locations[1].to_string())
print(second_wire.Locations[2].to_string())
