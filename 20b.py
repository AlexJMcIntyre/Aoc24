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
        self.cheat_neighbours = []

    def find_cheat_squares(self):
        for fs in (fs for fs in grid if fs.is_track):
            if abs(fs.x - self.x) + abs(fs.y-self.y) <= 20:
                self.cheat_neighbours.append((fs, abs(fs.x - self.x) + abs(fs.y-self.y)))


width = len(lines[0].strip())
height = len(lines)

print("loading grid")
grid = []
for line in enumerate(lines):
    for char in enumerate(line[1].strip()):
        grid.append(GridSquare(char[0], line[0], char[1]))


def find_track_by_coords(x, y):
    for fs in (g for g in grid if g.is_track):
        if fs.x == x and fs.y == y:
            return fs


def find_route(fs):
    for d in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        n = find_track_by_coords(fs.x + d[0], fs.y + d[1])
        if n is None:
            continue
        if n.distance is None:
            n.distance = fs.distance + 1
            return n


start = None
end = None

for s in grid:
    if s.is_start:
        start = s
    if s.is_end:
        end = s

print("routing")
leapfrog = start
while not end.distance:
    leapfrog = find_route(leapfrog)

print("finding neighbours")
for s in (s for s in grid if s.is_track):
    s.find_cheat_squares()

print("cheating")
score = 0
for s in (s for s in grid if s.is_track):
    for cheat in s.cheat_neighbours:
        if (cheat[0].distance - s.distance) - cheat[1] >= 100:
            score += 1

print('Total', score)
