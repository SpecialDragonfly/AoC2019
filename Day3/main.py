from Day3.Util import Util
from Day3.classes.Wire import Wire, Grid

util = Util()
values = util.parse('input.txt')
initial_wire = Wire()
initial_wire.trace(values[0])
second_wire = Wire()
second_wire.trace(values[1])
grid = Grid()
print("Closest: " + str(grid.intersect(initial_wire, second_wire)))
a = []
for intersection in grid.Intersections:
    d1 = initial_wire.distance_to(intersection)
    d2 = second_wire.distance_to(intersection)
    a.append([intersection, d1 + d2])

min = 9999
for x in a:
    if x[1] < min:
        min = x[1]
        print("Intersection " + x[0].to_string() + " was closer")

print(min)