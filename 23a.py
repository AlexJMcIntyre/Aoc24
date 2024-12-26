file = open("23_real.txt")
lines = file.readlines()


class Computer:
    def __init__(self, name):
        self.name = name
        self.neighbours = []

    def add_neighbour(self, n):
        if n not in self.neighbours:
            self.neighbours.append(n)


def find_comp_by_name(name):
    for fc in network:
        if fc.name == name:
            return fc
    network.append(Computer(name))
    return network[-1]


network = []

for line in lines:
    c1 = find_comp_by_name(line.strip().split("-")[0])
    c2 = find_comp_by_name(line.strip().split("-")[1])
    c1.add_neighbour(c2)
    c2.add_neighbour(c1)

sets = []

for c in network:
    for n in c.neighbours:
        for nn in n.neighbours:
            for nnn in nn.neighbours:
                if nnn == c:
                    net3 = tuple(sorted((c.name, n.name, nn.name)))
                    if net3 not in sets and ('t' == c.name[0] or 't' == n.name[0] or 't' == nn.name[0]):
                        sets.append(net3)

for s in sets:
    print(s)
print(len(sets))
