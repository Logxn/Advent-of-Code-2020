f = open("input.txt", "r")
data = f.read().split("\n")

preamble = data[:25]

# Remember day 1 ?
# New rule: The two numbers cannot be the same
def valid_num(num):
    for j in preamble:
        for k in preamble:
            if j != k:
                if int(j) + int(k) == int(num):
                    return True
                else:
                    continue
            else:
                continue
    return False

def solve(invalid_num):
    max_index = data.index(invalid_num)
    min_index = 0
    found = False

    while found == False:
        sum = 0

        for num in data[min_index:max_index]:
            curr_index = data.index(num)
            sum += int(num)

            if sum > int(invalid_num):
                min_index += 1
                break
            elif sum == int(invalid_num):
                max_index = data.index(num)

                results = list(map(int, data[min_index:max_index]))
                solution2 = min(results) + max(results)

                print(f'Solution 2: {solution2}')
                break
                
i = 25

while i < len(data):
    
    # Starting with the 26th number we need to move our preamble
    if i > 25:
        new_preamble = data[i - 25:i]
        preamble = new_preamble[:]
    
    result = valid_num(data[i])
    if result == False:
        print(f'Solution 1: {data[i]}')

        solve(data[i])
        break

    i += 1


