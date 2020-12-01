f = open("input.txt", "r")
input = f.read().split("\n")
numbers = list(map(int, input))

for i in numbers:
    for j in numbers:
        if i + j == 2020:
            solution1 = i * j
            break


for i in numbers:
    for j in numbers:
        for x in numbers:
            if i + j + x == 2020:
                solution2 = i * j * x
                break


print(solution1)
print(solution2)