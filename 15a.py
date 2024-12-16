file = open("15_real.txt")
lines = file.readlines()

grid = []  # grid is [y][x]
instructions = ''
moves = {"^": (-1, 0), "v": (+1, 0), "<": (0, -1), ">": (0, +1)}


for line in lines:
    if line[0] == '#':
        row = []
        for char in line.strip():
            row.append(char)
        grid.append(row)
    else:
        instructions = instructions + line.strip()


def print_grid():
    for fy in grid:
        print_row = ''
        for fx in fy:
            print_row += fx
        print(print_row)
    print()


def get_robot_coords():
    for fy in enumerate(grid):
        for fx in enumerate(fy[1]):
            if fx[1] == '@':
                return [fy[0], fx[0]]


def move(d):
    original = get_robot_coords()
    look = original.copy()
    possible = False
    to_move = []
    # look at squares in the direction we want to move
    while True:
        look[0] = look[0] + moves[d][0]
        look[1] = look[1] + moves[d][1]
        if grid[look[0]][look[1]] == '.':
            # ok to move
            possible = True
            break
        elif grid[look[0]][look[1]] == 'O':
            # add this box to list of things to move
            to_move.append([look[0], look[1]])
        elif grid[look[0]][look[1]] == '#':
            # wall before empty space, not possible
            possible = False
            break
        else:
            print("Nope!")
            break

    if possible:
        #  move the robot and everything in to_move
        grid[original[0]][original[1]] = '.'
        for b in to_move:
            grid[b[0]][b[1]] = '.'

        grid[original[0] + moves[d][0]][original[1] + moves[d][1]] = '@'
        for b in to_move:
            grid[b[0] + moves[d][0]][b[1] + moves[d][1]] = 'O'


for i in instructions:
    move(i)

print_grid()

score = 0
for y in enumerate(grid):
    for x in enumerate(y[1]):
        if x[1] == 'O':
            score += x[0] + 100 * y[0]
print(score)
