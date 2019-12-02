from Day2.Util import Util
from Day2.classes.IntCode import IntCode

util = Util()
values = util.parse('input.txt')
intCode = IntCode()
# 337042 + (noun * 19200) + verb = value
# 0, 0  -> 337042
# 1, 0  -> 567442
# 12, 0 -> 3101842
# 12, 2 -> 3101844
# 12, 3 -> 3101845
# 12, 4 -> 3101846
noun = 0
verb = 0
value = 0
wanted = 19690720
while value != wanted:
    value = intCode.compute(values.copy(), noun, verb)
    if value == wanted:
        print("-->", (100 * noun) + verb)
        break
    if value < wanted:
        if wanted - value < 19200:
            verb += 1
        elif wanted - value > 19200:
            noun += 1
    if value > wanted:
        if value - wanted > 19200:
            noun -= 1
        elif value - wanted < 19200:
            verb -= 1
