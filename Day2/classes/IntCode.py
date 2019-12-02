class IntCode:
    def compute(self, memory, noun, verb):
        memory[1] = noun
        memory[2] = verb
        for i in range(0, len(memory), 4):
            # instruction_pointer = i
            instruction = memory[i]
            # parameters
            first_value = memory[i + 1]
            second_value = memory[i + 2]
            answer_location = memory[i + 3]
            if instruction == 1:
                memory[answer_location] = memory[first_value] + memory[second_value]
            elif instruction == 2:
                memory[answer_location] = memory[first_value] * memory[second_value]
            elif instruction == 99:
                return memory[0]
