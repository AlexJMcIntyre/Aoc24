import copy

file = open("6_real.txt")
lines = file.readlines()

grid = []  # grid is [y][x]
moves = {
    "^": (-1, 0),
    "v": (+1, 0),
    "<": (0, -1),
    ">": (0, +1),
}

for line in lines:
    grid.append(list(line.strip()))

height = len(grid)
width = len(grid[0])


def find_guard(grid_local):  # find the guard's starting location:
    for y_local in enumerate(grid_local):
        for x_local in enumerate(y_local[1]):
            if x_local[1] in ("^", "v", "<", ">"):
                # we've recorded the guard location, so treat this as a normal visited space
                if x_local[1] in ("^", "v"):
                    grid_local[y_local[0]][x_local[0]] = '|'
                elif x_local[1] in ("<", ">"):
                    grid_local[y_local[0]][x_local[0]] = '-'
                return [y_local[0], x_local[0], x_local[1]]


def move_guard(guard_local, grid_local):
    global visited
    dy_local, dx_local = moves[guard_local[2]]
    ty = guard_local[0] + dy_local
    tx = guard_local[1] + dx_local
    if ty < 0 or tx < 0 or ty > height-1 or tx > width-1:
        # out of bounds, exit
        grid_local[ty - dy_local][tx - dx_local] = 'E'
        return 'exit'

    elif grid_local[ty][tx] in ('#', 'O'):
        # bump! rotate the guard and try again
        grid_local[ty - dy_local][tx - dx_local] = '+'
        if guard_local[2] == "^":
            guard_local[2] = ">"
        elif guard_local[2] == ">":
            guard_local[2] = "v"
        elif guard_local[2] == "v":
            guard_local[2] = "<"
        elif guard_local[2] == "<":
            guard_local[2] = "^"
        return 'moving'

    elif grid_local[ty][tx] in ("|", "-", '.', '+'):
        # move the guard
        guard_local[0] = ty
        guard_local[1] = tx
        # update the space
        if grid_local[ty][tx] == '+':
            # dunno. just roll with it.
            pass
        elif dy_local == 0 and grid_local[ty][tx] == '.':
            # we're moving horizontally into clean space
            grid_local[ty][tx] = '-'
            # visited += 1
        elif dy_local == 0 and grid_local[ty][tx] == '|':
            # we're moving horizontally into traversed space
            grid_local[ty][tx] = '+'
        elif dx_local == 0 and grid_local[ty][tx] == '.':
            # we're moving vertically into clean space
            grid_local[ty][tx] = '|'
            # visited += 1
        elif dx_local == 0 and grid_local[ty][tx] == '-':
            # we're moving vertically into traversed space
            grid_local[ty][tx] = '+'
        return 'moving'

    # elif grid_local[ty][tx] == '+':
    #     # uh-oh! We're looping
    #     return 'looping'

    else:
        print("unhandled location!")
        return False


def print_grid(grid_local):
    for row in grid_local:
        print(''.join(row))
    print()


def record_visit(guard_local, visited_local):
    if not (guard_local[0], guard_local[1]) in visited_local:
        visited_local.append((guard_local[0], guard_local[1]))


def test_maze(guard_local, grid_local, visited_local):
    i = 0
    while i < 10000:
        i += 1
        status = move_guard(guard_local, grid_local)
        record_visit(guard_local, visited_local)
        if status == 'exit':
            return 'exit'
        elif status == 'looping':
            return 'looping'
    return 'looping'


# find our starting location and record it
guard = find_guard(grid)

# begin vanilla pass through maze
v_guard = copy.deepcopy(guard)
v_grid = copy.deepcopy(grid)
visited = []

record_visit(v_guard, visited)

# walk through the maze step by step amd record our path
test_maze(v_guard, v_grid, visited)

print("visited", len(visited), "locations")

pos = 0
# for each visited space, add an obstacle and try again to see if it loops
perm = 0
for ob in visited:
    print("trying perm", perm)
    perm += 1
    t_guard = copy.deepcopy(guard)
    t_grid = copy.deepcopy(grid)
    t_grid[ob[0]][ob[1]] = 'O'
    t_status = test_maze(t_guard, t_grid, [])
    if t_status == 'looping':
        pos += 1

print(pos)
