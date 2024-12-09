file = open("9_real.txt")
lines = file.readlines()

disk_map = lines[0].strip()
disk = []
datamode = True
id_num = 0
for char in disk_map:
    for i in range(int(char)):
        if datamode:
            disk.append(id_num)
        else:
            disk.append('.')
    if datamode:
        id_num += 1
    datamode = not datamode


def check_disk():
    if [x for x in disk[disk.index('.'):] if not x == '.']:
        return False
    return True


while not check_disk():
    # find character to sort
    i = len(disk)-1
    while True:
        if not disk[i] == '.':
            break
        i -= 1
    tbs = disk.pop(i)
    disk.insert(i, '.')

    i = 0
    while True:
        if disk[i] == '.':
            break
        i += 1
    disk.pop(i)
    disk.insert(i, tbs)

result = 0
for c in enumerate(disk):
    if c[1] != '.':
        result += c[0]*c[1]

print(result)
