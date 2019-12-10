from Day9.Util import Util
from Day9.classes.IntCode import IntCode

util = Util()
values = util.parse('test1.txt')
print(values)

intCode = IntCode('Foo', values)
output = intCode.compute([1])
print(output)
