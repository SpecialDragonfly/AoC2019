class IntCode:
    def __init__(self, name, memory):
        self.Name = name
        self.InstructionPointer = 0
        self.Memory = memory
        self.Finished = False
        self.Phase = None
        self.RelativeBase = 0

    def resize_memory(self, location):
        if len(self.Memory) < location + 1:
            while len(self.Memory) < location + 1:
                self.Memory.append(0)

    def get_value(self, mode, value):
        if mode == 0:
            self.resize_memory(value)
            return self.Memory[value]
        if mode == 2:
            self.resize_memory(value + self.RelativeBase)
            return self.Memory[value + self.RelativeBase]
        else:
            return value

    def write_to_memory(self, mode, location, value):
        if mode == 2:
            location += self.RelativeBase
        elif mode == 1:
            print("Mode was 1 when writing")
        self.resize_memory(location)
        self.Memory[location] = value

    def handle_addition(self, parameter_modes):
        self.InstructionPointer += 1
        first_value = self.get_value(parameter_modes.pop(), self.Memory[self.InstructionPointer])
        self.InstructionPointer += 1
        second_value = self.get_value(parameter_modes.pop(), self.Memory[self.InstructionPointer])
        self.InstructionPointer += 1
        location = self.Memory[self.InstructionPointer]
        self.write_to_memory(parameter_modes.pop(), location, first_value + second_value)

    def handle_multiplication(self, parameter_modes):
        self.InstructionPointer += 1
        first_value = self.get_value(parameter_modes.pop(), self.Memory[self.InstructionPointer])
        self.InstructionPointer += 1
        second_value = self.get_value(parameter_modes.pop(), self.Memory[self.InstructionPointer])
        self.InstructionPointer += 1
        location = self.Memory[self.InstructionPointer]
        self.write_to_memory(parameter_modes.pop(), location, first_value * second_value)

    def handle_input(self, initial_input, parameter_modes):
        self.InstructionPointer += 1
        location = self.Memory[self.InstructionPointer]
        self.write_to_memory(parameter_modes.pop(), location, initial_input)

    def handle_output(self, parameter_modes):
        self.InstructionPointer += 1
        value = self.get_value(parameter_modes.pop(), self.Memory[self.InstructionPointer])
        return value

    def handle_jump_if_true(self, parameter_modes):
        self.InstructionPointer += 1
        first_value = self.get_value(parameter_modes.pop(), self.Memory[self.InstructionPointer])
        self.InstructionPointer += 1
        second_value = self.get_value(parameter_modes.pop(), self.Memory[self.InstructionPointer])
        if first_value != 0:
            self.InstructionPointer = second_value - 1

    def handle_jump_if_false(self, parameter_modes):
        self.InstructionPointer += 1
        first_value = self.get_value(parameter_modes.pop(), self.Memory[self.InstructionPointer])
        self.InstructionPointer += 1
        second_value = self.get_value(parameter_modes.pop(), self.Memory[self.InstructionPointer])
        if first_value == 0:
            self.InstructionPointer = second_value - 1

    def handle_less_than(self, parameter_modes):
        self.InstructionPointer += 1
        first_value = self.get_value(parameter_modes.pop(), self.Memory[self.InstructionPointer])
        self.InstructionPointer += 1
        second_value = self.get_value(parameter_modes.pop(), self.Memory[self.InstructionPointer])
        self.InstructionPointer += 1
        location = self.Memory[self.InstructionPointer]
        if first_value < second_value:
            self.write_to_memory(parameter_modes.pop(), location, 1)
        else:
            self.write_to_memory(parameter_modes.pop(), location, 0)

    def handle_equals(self, parameter_modes):
        self.InstructionPointer += 1
        first_value = self.get_value(parameter_modes.pop(), self.Memory[self.InstructionPointer])
        self.InstructionPointer += 1
        second_value = self.get_value(parameter_modes.pop(), self.Memory[self.InstructionPointer])
        self.InstructionPointer += 1
        location = self.Memory[self.InstructionPointer]
        if first_value == second_value:
            self.write_to_memory(parameter_modes.pop(), location, 1)
        else:
            self.write_to_memory(parameter_modes.pop(), location, 0)

    def handle_change_relative_base(self, parameter_modes):
        self.InstructionPointer += 1
        value = self.get_value(parameter_modes.pop(), self.Memory[self.InstructionPointer])
        self.RelativeBase += value

    def is_finished(self):
        return self.Finished

    def set_phase(self, phase):
        self.Phase = phase

    def get_phase(self):
        x = self.Phase
        self.Phase = None
        return x

    def compute(self, initial_input):
        output = []
        while True:
            instruction = str(self.Memory[self.InstructionPointer]).rjust(5, '0')
            opcode = int(instruction[-2:])
            parameter_modes = list(map(int, list(instruction[:-2])))
            if opcode == 1:
                self.handle_addition(parameter_modes)
            elif opcode == 2:
                self.handle_multiplication(parameter_modes)
            elif opcode == 3:
                value = self.get_phase()
                if value is None:
                    if len(initial_input) == 0:
                        # no available input, return the output
                        return output
                    else:
                        value = initial_input.pop()
                self.handle_input(value, parameter_modes)
            elif opcode == 4:
                x = self.handle_output(parameter_modes)
                output.append(x)
            elif opcode == 5:
                self.handle_jump_if_true(parameter_modes)
            elif opcode == 6:
                self.handle_jump_if_false(parameter_modes)
            elif opcode == 7:
                self.handle_less_than(parameter_modes)
            elif opcode == 8:
                self.handle_equals(parameter_modes)
            elif opcode == 9:
                self.handle_change_relative_base(parameter_modes)
            elif opcode == 99:
                self.Finished = True
                break
            self.InstructionPointer += 1
        return output

