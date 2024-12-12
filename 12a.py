file = open("12_real.txt")
lines = file.readlines()


class GridSquare:
    def __init__(self, x, y, label):
        self.x = x
        self.y = y
        self.label = label
        self.region = False


grid = []

# load squares into grid
for row in enumerate(lines):
    for char in enumerate(row[1].strip()):
        grid.append(GridSquare(char[0], row[0], char[1]))

height = len(lines)
width = len(lines[0]) - 1


# helper function to find squares by x, y
def find_square_by_coords(x, y):
    for g in grid:
        if g.x == x and g.y == y:
            return g
    return False


def find_unregioned_square():
    return next(s for s in grid if not s.region)


def mark_matching_neighbours(s_local):
    neighbours_local = [n for n in grid if n.label == s_local.label
                        and not n.region
                        and ((abs(n.x - s_local.x) == 1 and n.y == s_local.y) or (
                abs(n.y - s_local.y) == 1 and n.x == s_local.x))]
    if not neighbours_local:
        return
    for n in neighbours_local:
        n.region = s_local.region
        mark_matching_neighbours(n)  # oh, shit! recursion


def count_similar_neighbours(s):
    sn = 0
    for d in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        n = find_square_by_coords(s.x + d[0], s.y + d[1])
        if n:
            if n.region == s.region:
                sn += 1
    return sn


# region id
rid = 1

# work out all regions
while sum(not s.region for s in grid) > 0:
    cs = find_unregioned_square()
    cs.region = rid
    mark_matching_neighbours(cs)
    rid += 1

result = 0

# work out perimeters and then cost
for x in range(1, rid):
    squares = [s for s in grid if s.region == x]
    region_count = len(squares)
    region_perimeter = 0
    for s in squares:
        region_perimeter += 4 - count_similar_neighbours(s)
    result += region_count * region_perimeter

print(result)
