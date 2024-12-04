file = open("4_real.txt")
lines = file.readlines()

grid = []  # grid is [y][x]

result = 0


def direction_check(yl, xl):
    cc = grid[yl][xl]
    if cc != 'A':
        return False

    ctl = grid[yl - 1][xl - 1]
    ctr = grid[yl - 1][xl + 1]
    cbl = grid[yl + 1][xl - 1]
    cbr = grid[yl + 1][xl + 1]

    if ((ctl == 'M' and cbr == 'S') or (ctl == 'S' and cbr == 'M')) and ((cbl == 'M' and ctr == 'S') or (cbl == 'S' and ctr == 'M')):
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

for y in range(1, height-1):
    for x in range(1, width-1):
        if direction_check(y, x):
            result += 1

print(result)
