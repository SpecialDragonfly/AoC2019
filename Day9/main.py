from Day9.Util import Util
from Day9.classes.IntCode import IntCode

util = Util()
values = util.parse('input.txt')
intCode = IntCode("Foo", values)
output = intCode.compute([2])
print(output)

tests = [
    [109, -1, 4, 1, 99],  # -1
    [109, -1, 104, 1, 99],  # 1
    [109, -1, 204, 1, 99],  # 109
    [109, 1, 9, 2, 204, -6, 99],  # 204
    [109, 1, 109, 9, 204, -6, 99],  # 204
    [109, 1, 209, -1, 204, -106, 99],  # 204
    [109, 1, 3, 3, 204, 2, 99],  # input
    [109, 1, 203, 2, 204, 2, 99]  # input
]
for values in tests:
    print(values)
    intCode = IntCode('Foo', values)
    output = intCode.compute([5])
    print(output)



