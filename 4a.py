file = open("4_real.txt")
lines = file.readlines()

grid = []  # grid is [y][x]
directions = [(-1, -1),
              (-1, 0),
              (-1, +1),
              (0, -1),
              (0, +1),
              (+1, -1),
              (+1, 0),
              (+1, +1)]  # directions are [x][y]

result = 0


def direction_check(yl, xl, dir_local):
    dx = dir_local[0]
    dy = dir_local[1]
    if not (0 <= yl + (3 * dy) < width and 0 <= xl + (3 * dx) < height):
        return False
    c1 = grid[yl + (0 * dy)][xl + (0 * dx)]
    c2 = grid[yl + (1 * dy)][xl + (1 * dx)]
    c3 = grid[yl + (2 * dy)][xl + (2 * dx)]
    c4 = grid[yl + (3 * dy)][xl + (3 * dx)]
    if c1 + c2 + c3 + c4 == 'XMAS':
        # print("found at", xl, yl, "in direction", d)
        return True
    else:
        return False


for line in lines:
    line = line.strip()
    row = []
    for char in line:
        row.append(char)
    grid.append(row)

width = len(grid[0])
height = len(grid)

for y in range(height):
    for x in range(width):
        for d in directions:
            if direction_check(y, x, d):
                result += 1

print(result)
