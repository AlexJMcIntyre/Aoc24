file = open("2_real.txt")
lines = file.readlines()

safe = 0
for line in lines:
    line = line.strip().split()
    inc = 0
    dec = 0
    unsafe = 0
    for shift in range(len(line)-1):
        first = int(line[shift])
        second = int(line[shift+1])
        if first > second:
            dec = 1
        else:
            inc = 1
        if not 1 <= abs(first-second) <= 3:
            unsafe = 1
    if min(inc, dec) == 0 and unsafe == 0:
        safe += 1

print(safe)
