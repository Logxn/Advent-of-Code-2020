f = open("input.txt", "r")
game_input = f.read().split("\n")

def num_of_trees(right, down):
    found_trees = 0
    right_index = 0
    down_index = 0

    found = False

    while found == False:
        line = game_input[down_index]

        if right_index >= len(line):
            right_index %= len(line)

        if line[right_index] == '#':
            found_trees += 1

        right_index += right
        down_index += down

        if down_index >= len(game_input):
            found = True

    return found_trees

solution = num_of_trees(3,1)
solution2 = num_of_trees(3, 1) * num_of_trees(1,1) * num_of_trees(5,1) * num_of_trees(7,1) * num_of_trees(1, 2)
print(solution)
print(solution2)
