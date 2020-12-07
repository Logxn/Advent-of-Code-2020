import math

f = open("input.txt", "r")
boarding_passes = f.read().split("\n")

def find_missing(lst):
    return [x for x in range(lst[0], lst[-1]+1) if x not in lst]

ids = []
for boarding_pass in boarding_passes:
    boarding_pass = boarding_pass.replace("F", "0")
    boarding_pass = boarding_pass.replace("L", "0")
    boarding_pass = boarding_pass.replace("B", "1")
    boarding_pass = boarding_pass.replace("R", "1")

    ids.append(int(boarding_pass, 2))
    ids.sort()

print(find_missing(ids))