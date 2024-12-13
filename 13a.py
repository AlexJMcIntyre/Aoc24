file = open("13_real.txt")
lines = file.readlines()


class Machine:
    def __init__(self, fxa, fya, fxb, fyb, fxp, fyp):
        self.xa = fxa
        self.ya = fya
        self.xb = fxb
        self.yb = fyb
        self.xp = fxp
        self.yp = fyp


arcade = []
i = 0
while i < len(lines):
    xa = int(lines[i].strip().split("+")[1].split(",")[0])
    ya = int(lines[i].strip().split("+")[2])
    xb = int(lines[i+1].strip().split("+")[1].split(",")[0])
    yb = int(lines[i+1].strip().split("+")[2])
    xp = int(lines[i+2].strip().split("=")[1].split(",")[0])
    yp = int(lines[i+2].strip().split("=")[2])
    arcade.append(Machine(xa, ya, xb, yb, xp, yp))
    i += 4

score = 0
for m in arcade:
    best = False
    for a in range(101):
        for b in range(101):
            if (a * m.xa) + (b * m.xb) == m.xp and (a * m.ya) + (b * m.yb) == m.yp:
                # valid solution.
                if (not best) or (3*a + b) < best:
                    best = (3*a + b)
    if best:
        score += best

print(score)
