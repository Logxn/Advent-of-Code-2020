# Advent of Code 2020 - Day 1
# Task 1: Find two numbers that give 2020 if you add them up.
#         Then multiply them to get the solution for this task.
# Task 2: Find three number that give 2020 if you add them up.
#         Then multiply them to get the solution for this task.
#
# Note: This solution is quick and there might be better solutions. But it works.

f = open("input.txt", "r")
input = f.read().split("\n")
numbers = list(map(int, input)) # Convert the list of string numbers to a list of int numbers

# Task 1
for i in numbers:
    for j in numbers:
        if i + j == 2020:
            solution1 = i * j
            break

# Task 2
for i in numbers:
    for j in numbers:
        for x in numbers:
            if i + j + x == 2020:
                solution2 = i * j * x
                break


print(solution1)
print(solution2)