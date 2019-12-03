from functools import reduce

from Day3.Util import Util
from Day3.classes.Wire import Wire

util = Util()
values = util.parse('input.txt')
initial_wire = Wire()
initial_wire.trace(values[0])
print(len(initial_wire.locations()))
second_wire = Wire()
second_wire.trace(values[1])
print(len(second_wire.locations()))
print("Intersecting")
intersection = set(second_wire.locations()).union(initial_wire.locations())
print(len(intersection))

