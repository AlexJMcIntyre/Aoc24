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
def find_square_by_coords(x, y, grid_local):
    for g in grid_local:
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


def print_regions():
    for y in range(height):
        print_row = ''
        for x in range(width):
            c = find_square_by_coords(x, y, grid).region
            if c:
                print_row = print_row + str(c)
            else:
                print_row = print_row + '.'
        print(print_row)
    print()


def print_labels():
    for y in range(height):
        print_row = ''
        for x in range(width):
            c = find_square_by_coords(x, y, grid).label
            if c:
                print_row = print_row + str(c)
            else:
                print_row = print_row + '.'
        print(print_row)
    print()


def count_similar_neighbours(s):
    sn = 0
    for d in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        n = find_square_by_coords(s.x + d[0], s.y + d[1], grid)
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

score = 0

# work out number of sides, which is a perfectly normal metric. ugh.
for reg in range(1, rid):
    sides = 0
    squares = [s for s in grid if s.region == reg]
    x1 = height
    x2 = 0
    y1 = width
    y2 = 0
    for s in squares:
        x1 = min(x1, s.x)
        x2 = max(x2, s.x)
        y1 = min(y1, s.y)
        y2 = max(y2, s.y)

    # left perimeters

    for x in range(x1, x2+1):
        pen = False
        for y in range(y1, y2+1):
            candidate = find_square_by_coords(x, y, squares)
            if candidate:
                # check left is edge
                if not find_square_by_coords(x - 1, y, squares):
                    # yes, left edge
                    if not pen:
                        pen = True
                        sides += 1
                else:
                    # not an edge
                    pen = False
            else:
                # not a candidate
                pen = False

    # right perimeters
    for x in range(x1, x2+1):
        pen = False
        for y in range(y1, y2+1):
            candidate = find_square_by_coords(x, y, squares)
            if candidate:
                # check left is edge
                if not find_square_by_coords(x + 1, y, squares):
                    # yes, left edge
                    if not pen:
                        pen = True
                        sides += 1
                else:
                    # not an edge
                    pen = False

            else:
                # not a candidate
                pen = False

    # top perimeters
    for y in range(y1, y2+1):
        pen = False
        for x in range(x1, x2+1):
            candidate = find_square_by_coords(x, y, squares)
            if candidate:
                # check left is edge
                if not find_square_by_coords(x, y - 1, squares):
                    # yes, left edge
                    if not pen:
                        pen = True
                        sides += 1
                else:
                    # not an edge
                    pen = False

            else:
                # not a candidate
                pen = False

    # bottom perimeters
    for y in range(y1, y2+1):
        pen = False
        for x in range(x1, x2+1):
            candidate = find_square_by_coords(x, y, squares)
            if candidate:
                # check left is edge
                if not find_square_by_coords(x, y + 1, squares):
                    # yes, left edge
                    if not pen:
                        pen = True
                        sides += 1
                else:
                    # not an edge
                    pen = False

            else:
                # not a candidate
                pen = False

    score += sides*len(squares)

print(score)
