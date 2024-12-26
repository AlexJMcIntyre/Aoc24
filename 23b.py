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

# first find the sets of 3:
sets = []

for c in network:
    for n in c.neighbours:
        for nn in n.neighbours:
            for nnn in nn.neighbours:
                if nnn == c:
                    net3 = tuple(sorted((c.name, n.name, nn.name)))
                    if net3 not in sets:
                        sets.append(net3)

old_sets = sets

# for each set, try adding in each new member and see if it makes a set of 4:


def check_set_candidate(l_set, l_cand):  # set is tuple of names, candidate is computer
    global new_sets
    for lc in l_set:
        if l_cand not in find_comp_by_name(lc).neighbours:
            # this will not make a set.
            return False
    # all computers are linked to candidate, create a new set.
    tl = list(l_set)
    tl.append(l_cand.name)
    tl.sort()
    tl = tuple(tl)
    if tl not in new_sets:
        new_sets.append(tl)
    return True


print(3, len(old_sets))
i = 4
while len(old_sets) > 1:

    new_sets = []
    for s in old_sets:
        pot_cand = [c for c in network if c.name not in s]
        for p in pot_cand:
            check_set_candidate(s, p)
    old_sets = new_sets
    print(i, len(new_sets))
    i += 1

print(new_sets)
