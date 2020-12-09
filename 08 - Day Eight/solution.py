f = open("input.txt", "r")
instructions = f.read().split("\n")

def run(instruction_set):
    i = 0
    acc = 0
    seen_instructions = []
    seen = False

    while i < len(instruction_set):
        instruction = instruction_set[i][:3]
        value = int(instruction_set[i][4:])

        if seen == False and i in seen_instructions:
            print(f'Solution 1: {acc}')
            seen = True
        else:
            seen_instructions.append(i)

        # Note "nop" is not mentioned here as it should be ignored
        if instruction == "acc":
            acc += value
        elif instruction == "jmp":
            i += value - 1
        
        i += 1

run(instructions)