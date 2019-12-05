class IntCode:
    def __init__(self, memory):
        self.InstructionPointer = 0
        self.Memory = memory

    def get_value(self, mode, value):
        if mode == 0:
            return self.Memory[value]
        else:
            return value

    def handle_addition(self, parameter_modes):
        self.InstructionPointer += 1
        first_value = self.get_value(parameter_modes.pop(), self.Memory[self.InstructionPointer])
        self.InstructionPointer += 1
        second_value = self.get_value(parameter_modes.pop(), self.Memory[self.InstructionPointer])
        self.InstructionPointer += 1
        location = self.Memory[self.InstructionPointer]
        self.Memory[location] = first_value + second_value

    def handle_multiplication(self, parameter_modes):
        self.InstructionPointer += 1
        first_value = self.get_value(parameter_modes.pop(), self.Memory[self.InstructionPointer])
        self.InstructionPointer += 1
        second_value = self.get_value(parameter_modes.pop(), self.Memory[self.InstructionPointer])
        self.InstructionPointer += 1
        location = self.Memory[self.InstructionPointer]
        self.Memory[location] = first_value * second_value

    def handle_input(self, initial_input):
        self.InstructionPointer += 1
        location = self.Memory[self.InstructionPointer]
        self.Memory[location] = initial_input

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
            self.Memory[location] = 1
        else:
            self.Memory[location] = 0

    def handle_equals(self, parameter_modes):
        self.InstructionPointer += 1
        first_value = self.get_value(parameter_modes.pop(), self.Memory[self.InstructionPointer])
        self.InstructionPointer += 1
        second_value = self.get_value(parameter_modes.pop(), self.Memory[self.InstructionPointer])
        self.InstructionPointer += 1
        location = self.Memory[self.InstructionPointer]
        if first_value == second_value:
            self.Memory[location] = 1
        else:
            self.Memory[location] = 0

    def compute(self, initial_input):
        output = []
        while True:
            instruction = str(self.Memory[self.InstructionPointer]).rjust(5, '0')
            opcode = int(instruction[-2:])
            parameter_modes = list(map(int, list(instruction[:-2])))
            if opcode == 1:
                print("Handle addition")
                self.handle_addition(parameter_modes)
            elif opcode == 2:
                print("Handle multiplication")
                self.handle_multiplication(parameter_modes)
            elif opcode == 3:
                print("Handle input")
                self.handle_input(initial_input)
            elif opcode == 4:
                print("Handle output")
                x = self.handle_output(parameter_modes)
                output.append(x)
            elif opcode == 5:
                print("Jump if true")
                self.handle_jump_if_true(parameter_modes)
            elif opcode == 6:
                print("Jump if false")
                self.handle_jump_if_false(parameter_modes)
            elif opcode == 7:
                print("less check")
                self.handle_less_than(parameter_modes)
            elif opcode == 8:
                print("equals check")
                self.handle_equals(parameter_modes)
            elif opcode == 99:
                print("END")
                break
            self.InstructionPointer += 1
        return output

