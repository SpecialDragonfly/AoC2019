from Day10.Util import Util

util = Util()
values = util.parse("input.txt")
width = len(values[0])
height = len(values)
print("Width: ", width, "Height: ", height)
