from Day7.Util import Util
from Day7.classes.IntCode import IntCode

util = Util()
values = util.parse("input.txt")

scores = {}

phases = []
min_phase = 5
max_phase = 10

initial_input = 0
for phaseA in range(min_phase, max_phase):
    phases = [phaseA]
    for phaseB in range(min_phase, max_phase):
        if phaseB in phases:
            continue
        phases.append(phaseB)
        for phaseC in range(min_phase, max_phase):
            if phaseC in phases:
                continue
            phases.append(phaseC)
            for phaseD in range(min_phase, max_phase):
                if phaseD in phases:
                    continue
                phases.append(phaseD)
                for phaseE in range(min_phase, max_phase):
                    if phaseE in phases:
                        continue
                    phases.append(phaseE)
                    amp1 = IntCode("A", values.copy())
                    amp2 = IntCode("B", values.copy())
                    amp3 = IntCode("C", values.copy())
                    amp4 = IntCode("D", values.copy())
                    amp5 = IntCode("E", values.copy())
                    # print("Phases: ", phaseA, phaseB, phaseC, phaseD, phaseE)
                    amp1.set_phase(phaseA)
                    amp2.set_phase(phaseB)
                    amp3.set_phase(phaseC)
                    amp4.set_phase(phaseD)
                    amp5.set_phase(phaseE)
                    x = [initial_input]
                    while not amp5.is_finished():
                        outputA = amp1.compute(x)
                        outputB = amp2.compute(outputA)
                        outputC = amp3.compute(outputB)
                        outputD = amp4.compute(outputC)
                        x = amp5.compute(outputD)
                    scores["".join(map(str, phases))] = x
                    phases.pop()
                phases.pop()
            phases.pop()
        phases.pop()
    phases.pop()
print(max(scores.values()))