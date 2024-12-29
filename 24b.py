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
        s1 = get_node(self.i1).ov
        s2 = get_node(self.i2).ov
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


def get_node(l_ow):
    # returns a node for a given output name
    for g in graph:
        if g.ow == l_ow:
            return g


# load the graph
graph = []
for line in lines:
    if ":" in line:
        # first section
        g = Gate(line.strip().split(":")[0])

        graph.append(g)

    elif "->" in line:
        # second section
        g = Gate(line.strip().split(" ")[4])
        g.i1 = line.strip().split(" ")[0]
        g.i2 = line.strip().split(" ")[2]
        g.type = line.strip().split(" ")[1]
        graph.append(g)


def check_gate(i1, i2, g_type):
    for g in graph:
        if ((g.i1 == i1 and g.i2 == i2) or (g.i1 == i2 and g.i2 == i1)) and g.type == g_type:
            return g
    return False


# check gate 0:
print("half adder 0:")
xor1 = check_gate('x00', 'y00', 'XOR')
if xor1:
    print(xor1.ow, "is first XOR for input", 0)
else:
    print("error on XOR1", 0)
and1 = check_gate('x00', 'y00', 'AND')
if and1:
    print(and1.ow, "is first AND for input", 0)
else:
    print("error on AND1", 0)
print(and1.ow, "is carry for input", 0)
carry_out = and1
print()

swaps = []


def swap(n1, n2):
    global graph
    global swaps
    swaps.append(n1)
    swaps.append(n2)
    no1 = get_node(n1)
    no2 = get_node(n2)
    t1 = no1.ow
    t2 = no2.ow
    no1.ow = t2
    no2.ow = t1


swap('z15', 'fph')
swap('z21', 'gds')
swap('wrk', 'jrs')
swap('z34', 'cqk')


for i in range(1, 45):
    carry_in = carry_out
    print("full adder", i)
    xor1 = check_gate('x' + str(i).zfill(2), 'y' + str(i).zfill(2), 'XOR')
    if xor1:
        print(xor1.ow, "is first XOR for input", i)
    else:
        print("error on XOR1", i)
    and1 = check_gate('x' + str(i).zfill(2), 'y' + str(i).zfill(2), 'AND')
    if and1:
        print(and1.ow, "is first AND for input", i)
    else:
        print("error on AND1", i)
    xor2 = check_gate(xor1.ow, carry_in.ow, 'XOR')
    if xor2:
        print(xor2.ow, "is second XOR for input", i)
    else:
        print("error on XOR2", i)
    and2 = check_gate(xor1.ow, carry_in.ow, 'AND')
    if and2:
        print(and2.ow, "is second AND for input", i)
    else:
        print("error on AND2", i)
    or1 = check_gate(and2.ow, and1.ow, "OR")
    if or1:
        print(or1.ow, "is OR for input", i)
    else:
        print("error on OR", i)
    carry_out = or1
    print()

swaps = sorted(swaps)
print(swaps)
