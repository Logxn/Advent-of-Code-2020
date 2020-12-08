f = open("input.txt", "r")
instructions = f.read().split("\n")

acc = 0
seen = []

i = 0
while i < len(instructions):
    instruction = instructions[i][:3]
    value = int(instructions[i][4:])

    if i in seen:
        print(acc)
        break
    else:
        seen.append(i)

    if instruction == "acc":
        acc += value
    elif instruction == "jmp":
        i += value - 1
    else:
        i += 1
        continue

    i += 1