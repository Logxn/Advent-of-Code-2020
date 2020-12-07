import collections
from collections import OrderedDict  

f = open("input.txt", "r")
groups = f.read().split("\n\n")

def removeDupWithOrder(str):  
    return "".join(OrderedDict.fromkeys(str))

def duplicate_count(s):
    if len(s) == 1:
        return 1
    else:
        return len([x for x in set(s) if s.count(x) > 1])

def duplicate_raw():
    solution = 0
    for group in groups:
        answers = group.split("\n")
        
        intersections = set(answers[0]).intersection(*answers)
        solution += len(intersections)
    return solution

solution = 0

for group in groups:
    group = group.replace("\n", "")
    duplicates = duplicate_count(group)
    answer = removeDupWithOrder(group)

    solution += len(answer)

print(solution)
print(duplicate_raw())