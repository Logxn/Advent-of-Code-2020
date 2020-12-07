import collections
from collections import OrderedDict  

f = open("input.txt", "r")
groups = f.read().split("\n\n")

def removeDupWithOrder(str):  
    return "".join(OrderedDict.fromkeys(str))

solution = 0

for group in groups:
    group = group.replace("\n", "")
    answer = removeDupWithOrder(group)

    solution += len(answer)


print(solution)