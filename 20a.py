file = open("20_real.txt")
lines = file.readlines()


class GridSquare:
    def __init__(self, cx, cy, ct):
        self.x = int(cx)
        self.y = int(cy)
        self.is_wall = False
        self.is_track = False
        self.is_start = False
        self.is_end = False
        self.distance = None
        if ct == '#':
            self.is_wall = True
        elif ct == '.':
            self.is_track = True
        elif ct == 'S':
            self.is_track = True
            self.is_start = True
            self.distance = 0
        elif ct == 'E':
            self.is_track = True
            self.is_end = True


grid = []
for line in enumerate(lines):
    for char in enumerate(line[1].strip()):
        grid.append(GridSquare(char[0], line[0], char[1]))


def print_grid():
    for y in range(len(lines)):
        row = ''
        for x in range(len(lines[0].strip())):
            fs = find_track_by_coords(x, y)
            if fs.is_track:
                # row = row + str(fs.distance)
                row += '.'
            else:
                row = row + '#'
        print(row)
    print()


def find_track_by_coords(x, y):
    for fs in (g for g in grid if g.is_track):
        if fs.x == x and fs.y == y:
            return fs


def find_route(fs):
    for d in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        n = find_track_by_coords(fs.x + d[0], fs.y + d[1])
        if n is None:
            continue
        if n.distance is None and n.is_track:
            n.distance = fs.distance + 1
            return n


start = None
end = None

for s in grid:
    if s.is_start:
        start = s
    if s.is_end:
        end = s

leapfrog = start
while not end.distance:
    leapfrog = find_route(leapfrog)

# print_grid()
results = {}


def record_cheat(save):
    global results
    if save in results:
        results[save] += 1
    else:
        results[save] = 1


for s in (s for s in grid if s.is_track):
    for cheat in ((2, 0), (-2, 0), (0, 2), (0, -2)):  # , (1, 1), (1, -1), (-1, 1), (-1, -1)):
        jump = find_track_by_coords(s.x + cheat[0], s.y + cheat[1])
        if jump is None:
            continue
        if (jump.distance - s.distance)-2 >= 100:
            record_cheat((jump.distance - s.distance)-2)

sorted_scores = sorted(results.items(), key=lambda item: item[0])
total = 0
for r in sorted_scores:
    total += r[1]
    print(r[1], r[0])

print('Total', total)
