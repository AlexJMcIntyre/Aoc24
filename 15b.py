file = open("15_real.txt")
lines = file.readlines()

grid = []  # grid is [y][x]
instructions = ''
moves = {"^": (-1, 0), "v": (+1, 0), "<": (0, -1), ">": (0, +1)}


for line in lines:
    if line[0] == '#':
        row = []
        for char in line.strip():
            if char == '#':
                row.append('#')
                row.append('#')
            elif char == 'O':
                row.append('[')
                row.append(']')
            elif char == '.':
                row.append('.')
                row.append('.')
            elif char == '@':
                row.append('@')
                row.append('.')

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


to_move = []


def scan_ud(fy, fx, fd):
    global to_move
    ly = fy + moves[fd][0]
    lx = fx + moves[fd][1]

    if grid[ly][lx] == '.':
        return True
    elif grid[ly][lx] == '#':
        return False
    elif grid[ly][lx] == '[':
        if (ly, lx, '[') not in to_move:
            # add the found bracket
            to_move.append((ly, lx, '['))
            # search along from the bracket
            if not scan_ud(ly, lx, fd):
                return False
        if (ly, lx, ']') not in to_move:
            # add the paired bracket to the right
            to_move.append((ly, lx + 1, ']'))
            # search along from the paired bracket
            if not scan_ud(ly, lx + 1, fd):
                return False
    elif grid[ly][lx] == ']':
        if (ly, lx, ']') not in to_move:
            # add the found bracket
            to_move.append((ly, lx, ']'))
            # search along from the bracket
            if not scan_ud(ly, lx, fd):
                return False
        if (ly, lx, '[') not in to_move:
            # add the paired bracket to the left
            to_move.append((ly, lx - 1, '['))
            # search along from the paired bracket
            if not scan_ud(ly, lx - 1, fd):
                return False
    return True


def move(d):
    global to_move
    original = get_robot_coords()
    look = original.copy()
    possible = False
    to_move = []
    # look at squares in the direction we want to move
    if d in ("<", ">"):  # These directions move as in part a
        while True:
            look[0] = look[0] + moves[d][0]
            look[1] = look[1] + moves[d][1]
            if grid[look[0]][look[1]] == '.':
                # ok to move
                possible = True
                break
            elif grid[look[0]][look[1]] in ('[', ']'):
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

            if d == "<":
                p = "]"
            else:
                p = "["
            for b in to_move:
                grid[b[0] + moves[d][0]][b[1] + moves[d][1]] = p
                if p == "]":
                    p = "["
                else:
                    p = "]"
    else:  # moving up or down :(
        to_move = []
        if scan_ud(original[0], original[1], d):
            # clear the robot
            grid[original[0]][original[1]] = '.'
            # clear the boxes
            for b in to_move:
                grid[b[0]][b[1]] = '.'

            # move the robot
            grid[original[0] + moves[d][0]][original[1] + moves[d][1]] = '@'
            # move the boxes
            if to_move:
                for b in to_move:
                    grid[b[0] + moves[d][0]][b[1] + moves[d][1]] = b[2]


for i in enumerate(instructions):
    move(i[1])
    # print(i[0], i[1], ":")
    # print_grid()

score = 0
for y in enumerate(grid):
    for x in enumerate(y[1]):
        if x[1] == '[':
            score += x[0] + 100 * y[0]
print(score)
