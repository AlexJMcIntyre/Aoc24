file = open("10_real.txt")
lines = file.readlines()


class Pos:
    def __init__(self, fx, fy, fh):
        self.x = fx
        self.y = fy
        self.h = int(fh)
        self.walking = False
        self.score = 0


grid = []
width = len(lines[0].strip())
height = len(lines)

for line in enumerate(lines):
    for char in enumerate(line[1].strip()):
        grid.append(Pos(char[0], line[0], char[1]))


def get_pos_by_cood(fx,fy):
    for p in grid:
        if p.x == fx and p.y == fy:
            return p
    return False


def step_up(seg):
    # find all neighbours that are 1 step up
    for n in grid:
        if ((n.x == seg.x and abs(n.y - seg.y) == 1) or (n.y == seg.y and abs(n.x - seg.x) == 1)) and n.h == seg.h + 1:
            n.walking = True
    seg.walking = False


def print_grid():
    for y in range(height):
        row = ''
        for x in range(width):
            plot = get_pos_by_cood(x, y)
            if plot.walking:
                row = row + '*'
            else:
                row = row + str(plot.h)
        print(row)
    print()


score = 0

for pos in [pos for pos in grid if pos.h == 0]:
    # for all trailheads:
    pos.walking = True
    for i in range(9):
        for path in [path for path in grid if path.walking]:
            step_up(path)
    # done walking, count destinations
    score = score + len([des for des in grid if des.walking])


print(score)



