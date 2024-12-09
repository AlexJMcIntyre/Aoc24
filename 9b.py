import copy

file = open("9_real.txt")
lines = file.readlines()


class Seg:
    def __init__(self, id, size):
        self.id = id
        self.size = size


disk = []
datamode = True
id_num = 0

for char in lines[0].strip():
    if datamode:
        disk.append(Seg(id_num, int(char)))
        id_num += 1
    else:
        disk.append(Seg(-1, int(char)))
    datamode = not datamode


def disk_write():
    st = ''
    for s in disk:
        for c in range(s.size):
            if s.id == -1:
                st = st + '.'
            else:
                st = st + str(s.id)

    print(st)


def find_gap(size):
    for s in enumerate(disk):
        if s[1].size >= size and s[1].id == -1:
            return s[0]
    return False


def get_seg_by_id(id_local):
    for s in disk:
        if s.id == id_local:
            return s
    return False


id_num -= 1
disk_write()

while id_num >= 0:
    # first find the leftmost gap that will fit
    tbs = copy.copy(get_seg_by_id(id_num))  # seg to be sorted
    gap = find_gap(tbs.size)  # location of gap to fill
    if gap and gap < disk.index(get_seg_by_id(id_num)):
        pad = disk[gap].size - tbs.size  # padding that will be needed after insertion
        disk.pop(gap)  # remove the gap
        get_seg_by_id(id_num).id = -1  # also pop the tbs
        disk.insert(gap, tbs)
        if pad > 0:
            disk.insert(gap + 1, Seg(-1, pad))
    # disk_write()
    id_num -= 1

dlist = []
for s in disk:
    for x in range(s.size):
        if s.id == -1:
            dlist.append('.')
        else:
            dlist.append(s.id)

result = 0
for c in enumerate(dlist):
    if c[1] != '.':
        result += c[0]*c[1]

print(result)

