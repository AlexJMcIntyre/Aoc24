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
visited = 1


def find_guard():  # find the guard's starting location:
    for y in enumerate(grid):
        for x in enumerate(y[1]):
            if x[1] in ("^", "v", "<", ">"):
                grid[y[0]][x[0]] = 'X' # we've recorded the guard location, so treat this as a normal visited space
                return [y[0], x[0], x[1]]


def move_guard(guard_local):
    global visited
    dy, dx = moves[guard_local[2]]
    ty = guard_local[0] + dy
    tx = guard_local[1] + dx
    if ty < 0 or tx < 0 or ty > height-1 or tx > width-1:
        # out of bounds, exit
        return False
    elif grid[ty][tx] == '.':
        # move the guard
        guard_local[0] = ty
        guard_local[1] = tx
        # count the visit
        visited += 1
        # update the space
        grid[ty][tx] = 'X'
        return True
    elif grid[ty][tx] == 'X':
        # move the guard
        guard_local[0] = ty
        guard_local[1] = tx
        return True
    elif grid[ty][tx] == '#':
        if guard[2] == "^":
            guard[2] = ">"
        elif guard[2] == ">":
            guard[2] = "v"
        elif guard[2] == "v":
            guard[2] = "<"
        elif guard[2] == "<":
            guard[2] = "^"
        return True
    else:
        print("unhandled location!")
        return False


guard = find_guard()
while move_guard(guard):
    pass  # moving...

print(visited)

