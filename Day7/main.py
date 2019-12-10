from Day7.Util import Util
from Day7.classes.IntCode import IntCode

util = Util()
values = util.parse("test4.txt")

scores = {}

phases = []
min_phase = 5
max_phase = 10

amp1 = IntCode(values)
amp2 = IntCode(values)
amp3 = IntCode(values)
amp4 = IntCode(values)
amp5 = IntCode(values)

initial_input = 0
for phaseA in range(min_phase, max_phase):
    phases = [phaseA]
    x = [initial_input, phaseA]
    outputA = amp1.compute(x)
    for phaseB in range(min_phase, max_phase):
        if phaseB in phases:
            continue
        phases.append(phaseB)
        outputB = amp2.compute([outputA[0], phaseB])
        for phaseC in range(min_phase, max_phase):
            if phaseC in phases:
                continue
            phases.append(phaseC)
            outputC = amp3.compute([outputB[0], phaseC])
            for phaseD in range(min_phase, max_phase):
                if phaseD in phases:
                    continue
                phases.append(phaseD)
                outputD = amp4.compute([outputC[0], phaseD])
                for phaseE in range(min_phase, max_phase):
                    if phaseE in phases:
                        continue
                    phases.append(phaseE)
                    initial_input = amp5.compute([outputD[0], phaseE])[0]
                    print("E output: ", initial_input)
                    phases.pop()
                phases.pop()
            phases.pop()
        phases.pop()
    phases.pop()
