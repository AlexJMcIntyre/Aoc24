from copy import deepcopy
file = open("21_real.txt")
lines = file.readlines()


class Keypad:
    def __init__(self, ck, ct):
        self.keys = ck  # remember keys is [y][x]
        self.finger = self.find_key('A')
        self.type = ct

    def find_key(self, desired):
        for y in enumerate(self.keys):
            for x in enumerate(y[1]):
                if x[1] == desired:
                    return x[0], y[0]

    def move_to(self, desired):
        move_str = ''
        d = self.find_key(desired)
        move = d[0] - self.finger[0], d[1] - self.finger[1]

        def move_u(i):
            if i[1] < 0:
                return abs(i[1]) * '^'
            else:
                return ''

        def move_d(i):
            if i[1] > 0:
                return abs(i[1]) * 'v'
            else:
                return ''

        def move_l(i):
            if i[0] < 0:
                return abs(i[0]) * '<'
            else:
                return ''

        def move_r(i):
            if i[0] > 0:
                return abs(i[0]) * '>'
            else:
                return ''

        if self.type == 'n':
            # numeric pad, hazard is moving left or down into gap
            # check left hazard (ie on bottom row, looking to move to left col):
            if self.finger[1] == 3 and d[0] == 0:
                # in this case, move up, left
                move_str += move_u(move)
                move_str += move_l(move)

            # check down hazard (ie in left col, looking to move down to bottom):
            elif self.finger[0] == 0 and d[1] == 3:
                # right, down
                move_str += move_r(move)
                move_str += move_d(move)

            # otherwise, a normal move
            else:
                move_str += move_l(move)
                move_str += move_u(move)
                move_str += move_d(move)
                move_str += move_r(move)

        elif self.type == 'd':
            # dpad, hazard is moving left or up into gap
            # check left hazard (ie on top row, looking to move to left col):
            if self.finger[1] == 0 and d[0] == 0:
                # in this case, move down, left
                move_str += move_d(move)
                move_str += move_l(move)

            # check up hazard (ie in left col, looking to move up to top):
            elif self.finger[0] == 0 and d[1] == 0:
                # right, up
                move_str += move_r(move)
                move_str += move_u(move)

            # otherwise, a normal move
            else:
                move_str += move_l(move)
                move_str += move_u(move)
                move_str += move_d(move)
                move_str += move_r(move)

        self.finger = d
        return move_str + 'A'


door = Keypad([['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], [None, '0', 'A']], 'n')
dpad1 = Keypad([[None, '^', 'A'], ['<', 'v', '>']], 'd')
dpad2 = Keypad([[None, '^', 'A'], ['<', 'v', '>']], 'd')


def get_move_seq(l_object, l_seq):
    l_moves = []
    for l_s in l_seq:
        l_moves.append(l_object.move_to(l_s))
    return l_moves

move_counter = {}

def add_move_to_counter(f_move, f_add):
    global move_counter
    if f_move in move_counter:
        move_counter[f_move] += f_add
    else:
        move_counter[f_move] = f_add



results = 0
for line in lines:
    door_code = line.strip()
    multiplier = int(''.join([c for c in door_code if c.isnumeric()]))

    # initial num pad on dpad 1
    for r in get_move_seq(door, door_code):
        add_move_to_counter(r, 1)
    # print(multiplier, '*', len(r))
    print(move_counter)
    # results += multiplier * len(r)

    for i in range(25):
    #num pad n on num pad n+1
        these_moves = deepcopy(move_counter)
        move_counter = {}
        for m in these_moves:
            for r in get_move_seq(dpad1,m):
                add_move_to_counter(r,these_moves[m])

    # calculate results
    length = 0
    for m in move_counter:
        length += (len(m) * move_counter[m])
    print(length * multiplier)
    print(move_counter)
    results += length * multiplier
    move_counter = {}

print(results)
