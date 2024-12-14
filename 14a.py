file = open("14_real.txt")
lines = file.readlines()

width = 101
height = 103


class Robot:
    def __init__(self, cx, cy, cdx, cdy):
        self.x = cx
        self.y = cy
        self.dx = cdx
        self.dy = cdy


robots = []

for line in lines:
    seg = line.strip().split(" ")
    x = int(seg[0].split(",")[0][2:])
    y = int(seg[0].split(",")[1])
    dx = int(seg[1].split(",")[0][2:])
    dy = int(seg[1].split(",")[1])
    robots.append(Robot(x, y, dx, dy))


def print_grid():
    for y in range(height):
        row = ''
        for x in range(width):
            count = len([r for r in robots if r.x == x and r.y == y])
            if count == 0:
                if x == int(width/2) or y == int(height/2):
                    row = row + ' '
                else:
                    row = row + '.'
            else:
                row = row + str(count)
        print(row)


seconds = 100
q = [0, 0, 0, 0]

for r in robots:
    r.x = (r.x + r.dx * seconds) % width
    r.y = (r.y + r.dy * seconds) % height

    if r.x < int(width/2) and r.y < int(height/2):
        q[0] += 1
    elif r.x > int(width / 2) and r.y < int(height / 2):
        q[1] += 1
    elif r.x < int(width / 2) and r.y > int(height / 2):
        q[2] += 1
    elif r.x > int(width / 2) and r.y > int(height / 2):
        q[3] += 1

print_grid()

print(q)
print(q[0] * q[1] * q[2] * q[3])
