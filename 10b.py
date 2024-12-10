file = open("10_real.txt")
lines = file.readlines()


class Pos:
    def __init__(self, fx, fy, fh):
        self.x = fx
        self.y = fy
        if fh != '.':
            self.h = int(fh)
        else:
            self.h = -1
        self.walking = 0


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


def print_grid():
    for y in range(height):
        row = ''
        for x in range(width):
            plot = get_pos_by_cood(x, y)
            if plot.walking == 1:
                row = row + '*'
            elif plot.walking == 2:
                row = row + '#'
            elif plot.walking > 2:
                row = row + '~'
            elif plot.h == -1:
                row = row + '.'
            else:
                row = row + str(plot.h)
        print(row)
    print()


def step_up(seg):
    global score
    # find all neighbours that are 1 step up
    neighbours = [n for n in grid if ((n.x == seg.x and abs(n.y - seg.y) == 1) or (n.y == seg.y and abs(n.x - seg.x) == 1)) and n.h == seg.h + 1]
    for n in neighbours:
        n.walking += 1
        score += 1
    seg.walking = 0
    score -= 1


score = 0
scorecard = []
for pos in [pos for pos in grid if pos.h == 0]:
    # for all trailheads:
    pos.walking = 1
    score += 1
    for i in range(9):
        for path in [path for path in grid if path.walking > 0]:
            for r in range(path.walking):
                step_up(path)
    # done walking, count destinations

    scorecard.append(score)

print(sum(scorecard))