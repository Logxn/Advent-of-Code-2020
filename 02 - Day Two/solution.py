# Advent of Code - Day 2
# Task(s): Verify passwords with given password policies
#
# Note: This solution is quick and dirty and there might be a better solution.
#       But it works ;)

def check_validity(policy, min_count, max_count, password):
    count = 0

    for c in password:
        if c == policy:
            count += 1
    
    # Min-Max verification
    if count >= int(min_count) and count <= int(max_count):
        return True
    
    return False

def check_validtiy_new(policy, min_count, max_count, password):
    # All countings start at 1
    pos1 = int(min_count) - 1
    pos2 = int(max_count) - 1

    
    if password[pos1] != policy and password[pos2] != policy: # No position contains the policy letter
        return False
    elif password[pos1] == policy and password[pos2] != policy: # One of the position does contain the letter
        return True
    elif password[pos1] != policy and password[pos2] == policy: # One of the position does contain the letter
        return True
    elif password[pos1] == policy and password[pos2] == policy: # Both positions contain the letter
        return False

f = open("input.txt", "r")
password_policies = f.read().split("\n")

password_ranges = []
policies = []
passwords = []

for line in password_policies:
    breakdown = line.split(" ")

    password_ranges.append(breakdown[0].split("-"))
    policies.append(breakdown[1].replace(":", ""))
    passwords.append(breakdown[2])

solution = 0
solution2 = 0

for i in range(len(passwords)):
    policy = policies[i]
    min_count = password_ranges[i][0]
    max_count = password_ranges[i][1]
    password = passwords[i]

    verify = check_validity(policy, min_count, max_count, password)
    verify2 = check_validity_new(policy, min_count, max_count, password)
    if verify == True:
        solution += 1
    if verify2 == True:
        solution2 += 1

print(solution)
print(solution2)

