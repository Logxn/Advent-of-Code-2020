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
            print(f'Looped at Acc-Value: {acc}')
            seen = True
            break
        else:
            seen_instructions.append(i)

        # Note "nop" is not mentioned here as it should be ignored
        if instruction == "acc":
            acc += value
        elif instruction == "jmp":
            i += value - 1
        
        i += 1

    if seen == False:
        print(f'Solution 2: {acc}')
        return True

    return False

replaced_indexes = []
def run_pt2():
    i = 0

    # It is necessary to always reset our instruction set
    # Otherwise replacements won't be deleted
    # 
    # Thank you @JanEtschel for showing me how to hard copy an array
    # Not hard copying the array will result in a stack-overflow
    instruction_set = instructions[:]

    while i < len(instructions):
        instruction = instruction_set[i]

        # We already tried to replace this index
        # Assuming our run function looped and returned false
        # We do not want to try and replace said index
        if i in replaced_indexes:
            i += 1
            continue
        
        # Our mission is to replace exactly ONE instruction
        # nop -> jmp and vice versa
        #
        # After the replacement the seen index will be added to the "replaced_indexes" list
        # If run fails we already know what we replaced and carry on with the next relevant instruction
        if instruction[:3] == "nop":
            instruction_set[i] = instruction.replace("nop", "jmp")
            replaced_indexes.append(i)
            break
        elif instruction[:3] == "jmp":
            instruction_set[i] = instruction.replace("jmp", "nop")
            replaced_indexes.append(i)
            break

        i += 1
    
    result = run(instruction_set)
    if result == False:
        return run_pt2()

run(instructions)
run_pt2()