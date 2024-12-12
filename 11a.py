file = open("11_real.txt")
line = file.read()


class Hopper:
    def __init__(self, marker):
        self.marker = marker  # the number engraved on the stones
        self.stones_now = 0  # number of stones in the hopper
        self.stones_next = 0  # stones added during the blink
        if self.marker == 0:
            self.output = (1,)
        elif len(str(self.marker)) % 2 == 0:
            # even
            marker_str = str(self.marker)
            midpoint = int(len(marker_str) / 2)
            self.output = (int(marker_str[:midpoint]), int(marker_str[midpoint:]))
        else:
            self.output = (self.marker * 2024,)

    def reset(self):
        self.stones_now = self.stones_next
        self.stones_next = 0

    def blink(self):
        for o in self.output:
            load_hopper(o, self.stones_now)


hopper_list = []


def find_hopper(marker):
    # return hopper if exists, or create and return if not
    for h in hopper_list:
        if h.marker == marker:
            return h
    hopper_list.append(Hopper(marker))
    return hopper_list[-1]


def load_hopper(marker, stones):
    find_hopper(marker).stones_next += stones


def print_list():
    for h in [h for h in hopper_list if h.stones_now != 0]:
        print(h.stones_now, 'x', h.marker)
    print()


# load initial stones
for s in line.strip().split():
    load_hopper(int(s), 1)

# initial reset
for h in hopper_list:
    h.reset()

for blinks in range(25):
    for h in [h for h in hopper_list if h.stones_now != 0]:
        h.blink()
    for h in hopper_list:
        h.reset()

result = 0
for h in hopper_list:
    result += h.stones_now

print(result)
