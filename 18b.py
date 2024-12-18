file = open("18_real.txt")
lines = file.readlines()

height = 71
width = 71
fallen_bytes = 2872

grid = []


class GridSquare:
    def __init__(self, fx, fy):
        self.x = fx
        self.y = fy
        self.distance = float('inf')
        self.visited = False
        self.corrupted = False
        self.neighbours = None

    def find_neighbours(self):
        self.neighbours = []

        for d in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            pn = find_square_by_coords(self.x + d[0], self.y + d[1])
            if pn and not pn.corrupted:
                self.neighbours.append(pn)


def find_square_by_coords(fx, fy):
    for s in grid:
        if s.x == fx and s.y == fy:
            return s
    return False


def print_grid():
    for fy in range(height):
        row = ''
        for fx in range(width):
            fs = find_square_by_coords(fx, fy)
            if fs.corrupted:
                row += '#'
            elif fs.visited:
                row += 'O'
            else:
                row += '.'
        print(row)
    print()


def find_closest_unvisited():
    u = [u for u in grid if not u.visited]
    if u:
        u.sort(key=lambda square: square.distance)
        return u[0]


for x in range(width):
    for y in range(height):
        grid.append(GridSquare(x, y))

# load starting square:
    find_square_by_coords(0, 0).distance = 0

for i in range(fallen_bytes):
    x = int(lines[i].strip().split(",")[0])
    y = int(lines[i].strip().split(",")[1])
    find_square_by_coords(x, y).corrupted = True
    print("dropping byte ", x, y)

print_grid()

for s in grid:
    s.find_neighbours()

while len([u for u in grid if not u.visited]) > 0:
    v = find_closest_unvisited()
    for n in v.neighbours:
        new_dist = min(v.distance + 1, n.distance)
        n.distance = new_dist
    v.visited = True
    if v.x == width-1 and v.y == height-1:
        break

print(find_square_by_coords(width-1, height-1).distance)

