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
        for d in range(1, width):
            check_antinode((d*b.x - (d-1)*a.x, d*b.y - (d-1)*a.y))
            check_antinode((d*a.x - (d-1)*b.x, d*a.y - (d-1)*b.y))

print(antinodes)
print(len(antinodes))