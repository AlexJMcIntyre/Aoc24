file = open("24_real.txt")
lines = file.readlines()


class Gate:
    def __init__(self, ow):
        self.i1 = None
        self.i2 = None
        self.type = None
        self.ov = None  # output value
        self.ow = ow  # output wire

    def output(self):
        s1 = find_output(self.i1)
        s2 = find_output(self.i2)
        if s1 is not None and s2 is not None:
            if self.type == 'AND':
                if s1 == 1 and s2 == 1:
                    self.ov = 1
                else:
                    self.ov = 0
            elif self.type == 'OR':
                if s1 == 1 or s2 == 1:
                    self.ov = 1
                else:
                    self.ov = 0
            elif self.type == 'XOR':
                if s1 != s2:
                    self.ov = 1
                else:
                    self.ov = 0
        else:
            # not ready yet
            pass


def find_output(l_output):
    for g in graph:
        if g.ow == l_output:
            return g.ov


graph = []
for line in lines:
    if ":" in line:
        # first section
        g = Gate(line.strip().split(":")[0])
        g.ov = int(line.strip().split(":")[1])
        graph.append(g)

    elif "->" in line:
        # second section
        g = Gate(line.strip().split(" ")[4])
        g.i1 = line.strip().split(" ")[0]
        g.i2 = line.strip().split(" ")[2]
        g.type = line.strip().split(" ")[1]
        graph.append(g)

unsolved = [g for g in graph if g.ov is None]
while len(unsolved) > 0:
    for ug in unsolved:
        ug.output()
    unsolved = [g for g in graph if g.ov is None]

results = []
for g in graph:
    if 'z' in g.ow:
        results.append((g.ow, g.ov))

results = sorted(results, key=lambda x: x[0], reverse=True)

res_str = ''
for r in results:
    res_str += str(r[1])

print(int(res_str, 2))
