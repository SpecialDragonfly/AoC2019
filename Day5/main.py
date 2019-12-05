from Day5.Util import Util
from Day5.classes.IntCode import IntCode

util = Util()
values = util.parse('input.txt')
intcode = IntCode(values)
print(intcode.compute(5))
