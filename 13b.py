file = open("13_real.txt")
lines = file.readlines()


class Machine:
    def __init__(self, fxa, fya, fxb, fyb, fxp, fyp):
        self.xa = fxa
        self.ya = fya
        self.xb = fxb
        self.yb = fyb
        self.xp = fxp + 10000000000000
        self.yp = fyp + 10000000000000


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
    b = round((m.xp-(m.xa*m.yp/m.ya))/((-m.xa*m.yb/m.ya)+m.xb), 3)
    if b.is_integer():
        a = round((m.xp - b*m.xb)/m.xa, 3)
        if a.is_integer():
            score += 3*a + b

print(score)
