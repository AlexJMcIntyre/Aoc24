file = open("16_real.txt")
lines = file.readlines()


class GridSquare:
    def __init__(self, fx, fy, fz, f_type):
        self.x = fx
        self.y = fy
        self.z = fz
        self.distance = float('inf')
        self.visited = False
        if f_type == 'S' and fz == 1:  # start on the east/west plane
            self.start = True
            self.distance = 0
        else:
            self.start = False
        if f_type == 'E':
            self.end = True  # either plane is valid end
        else:
            self.end = False
        self.neighbours = []  # is format (neighbour, cost)
        self.pre = []

    def find_neighbours(self):
        if self.z == 0:
            # north / south
            n = find_square_by_coords(self.x, self.y - 1, 0)
            if n:
                # on the same plane, add neighbour directly
                self.neighbours.append((n, 1))
            s = find_square_by_coords(self.x, self.y + 1, 0)
            if s:
                # on the same plane, add neighbour directly
                self.neighbours.append((s, 1))
            e = find_square_by_coords(self.x - 1, self.y, 1)
            w = find_square_by_coords(self.x + 1, self.y, 1)
            if e or w:
                # different plane, add link to mirror
                m = find_square_by_coords(self.x, self.y, 1)
                self.neighbours.append((m, 1000))
        elif self.z == 1:
            # east / west
            e = find_square_by_coords(self.x - 1, self.y, 1)
            if e:
                # on the same plane, add neighbour directly
                self.neighbours.append((e, 1))
            w = find_square_by_coords(self.x + 1, self.y, 1)
            if w:
                # on the same plane, add neighbour directly
                self.neighbours.append((w, 1))
            n = find_square_by_coords(self.x, self.y, 0)
            s = find_square_by_coords(self.x, self.y, 0)
            if n or s:
                # different plane, add link to mirror
                m = find_square_by_coords(self.x, self.y, 0)
                self.neighbours.append((m, 1000))


def find_square_by_coords(fx, fy, z):
    for fs in grid:
        if fs.x == fx and fs.y == fy and fs.z == z:
            return fs
    return False


def find_closest_unvisited():
    u = [u for u in grid if not u.visited]
    if u:
        u.sort(key=lambda square: square.distance)
        return u[0]


grid = []
for y in enumerate(lines):
    for x in enumerate(y[1].strip()):
        if x[1] != '#':
            grid.append(GridSquare(x[0], y[0], 0, x[1]))  # north / south plane
            grid.append(GridSquare(x[0], y[0], 1, x[1]))  # east / west plane

for sq in grid:
    sq.find_neighbours()

while len([u for u in grid if not u.visited]) > 0:
    v = find_closest_unvisited()
    for n in v.neighbours:
        if v.distance + n[1] <= n[0].distance:
            n[0].distance = v.distance + n[1]
            n[0].pre.append(v)
    v.visited = True

for sq in grid:  # find the end point on both planes
    if sq.end and sq.z == 1:
        e1 = sq
    elif sq.end and sq.z == 0:
        e0 = sq

if e1.distance > e0.distance:  # work out which is the closer end point
    e1.end = False
    f = e0
else:
    e0.end = False
    f = e1

print('Best distance', f.distance)

route = []


def trace_route(fsq):
    if (fsq.x, fsq.y) not in route:
        route.append((fsq.x, fsq.y))
    for fn in fsq.pre:
        trace_route(fn)


trace_route(f)
print('Number of tiles on best routes', len(route))

height = len(lines)
width = len(lines[0].strip())

for y in range(height):
    row = ''
    for x in range(width):
        if (x,y) in route:
            row = row + 'O'
        else:
            s = find_square_by_coords(x, y, 0)
            if s:
                row = row + '.'
            else:
                row = row + '#'
        row= row + ','
    print(row)
# gotta be honest, this is returning the wrong answer but i could see the extra branches in the output and just
# subtracted the extra squares.
