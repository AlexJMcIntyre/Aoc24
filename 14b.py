import statistics

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
                row = row + '.'
            else:
                row = row + str(count)
        print(row)


seconds = 1
x_sd_list = []
y_sd_list = []

for i in range(10000):
    x_list = []
    y_list = []
    for r in robots:
        r.x = (r.x + r.dx * seconds) % width
        r.y = (r.y + r.dy * seconds) % height
        x_list.append(r.x)
        y_list.append(r.y)
    x_sd_list.append(statistics.stdev(x_list))
    y_sd_list.append(statistics.stdev(y_list))
    i += 1

for i in range(10000):
    print(x_sd_list[i], y_sd_list[i])

