file = open("25_real.txt")
lines = file.readlines()

keys = []
locks = []


class Key:
    def __init__(self, t0, t1, t2, t3, t4):
        self.t = [t0, t1, t2, t3, t4]


class Lock:
    def __init__(self, t0, t1, t2, t3, t4):
        self.t = [t0, t1, t2, t3, t4]


def read_schematic(l0, l1, l2, l3, l4, l5, l6):
    p0 = [l0[0], l1[0], l2[0], l3[0], l4[0], l5[0], l6[0]].count("#") - 1
    p1 = [l0[1], l1[1], l2[1], l3[1], l4[1], l5[1], l6[1]].count("#") - 1
    p2 = [l0[2], l1[2], l2[2], l3[2], l4[2], l5[2], l6[2]].count("#") - 1
    p3 = [l0[3], l1[3], l2[3], l3[3], l4[3], l5[3], l6[3]].count("#") - 1
    p4 = [l0[4], l1[4], l2[4], l3[4], l4[4], l5[4], l6[4]].count("#") - 1
    if l0[0] == '.':
        keys.append(Key(p0, p1, p2, p3, p4))
    elif l0[0] == '#':
        locks.append(Lock(p0, p1, p2, p3, p4))


for i in range(0, len(lines), 8):
    read_schematic(lines[i + 0], lines[i + 1], lines[i + 2], lines[i + 3],
                   lines[i + 4], lines[i + 5], lines[i + 6])


def check_overlap(fl, fk):
    if max([sum(x) for x in zip(fl.t, fk.t)]) <= 5:
        return True
    else:
        return False


results = 0
for l in locks:
    for k in keys:
        r = check_overlap(l, k)
        if r:
            print("lock", l.t, "and key", k.t, ": all columns fit")
            results += 1
        else:
            print("lock", l.t, "and key", k.t, ": overlap")
print(results)
