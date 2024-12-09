file = open("8_real.txt")
lines = file.readlines()


class Antenna:
    def __init__(self, x, y, f):
        self.x = x
        self.y = y
        self.freq = f


antennae = []

width = len(lines[0].strip())
height = len(lines)

for line in enumerate(lines):
    for char in enumerate(line[1].strip()):
        if char[1] != '.':
            antennae.append(Antenna(char[0], line[0], char[1]))


antinodes = []


def check_antinode(a_local):
    global antinodes
    if not 0 <= a_local[0] < width:
        return False
    if not 0 <= a_local[1] < height:
        return False
    if a_local not in antinodes:
        antinodes.append(a_local)


for a in antennae:
    for b in (b for b in antennae if b != a and b.freq == a.freq):
        check_antinode((2*b.x - a.x, 2*b.y-a.y))
        check_antinode((2*a.x - b.x, 2*a.y - b.y))

print(antinodes)
print(len(antinodes))