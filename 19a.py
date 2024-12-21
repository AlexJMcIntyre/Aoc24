file = open("19_real.txt")
lines = file.readlines()


def solve(design_local):
    global cache
    if design_local in cache:
        return False
    for t in towels:
        # try a towel from our pool and see if it fits the first part of the design.
        if design_local[:len(t)] == t:
            # it does fit! Is this all the design?
            if design_local[len(t):] == '':
                # it is! Success
                return True
            else:
                # not there yet,send the remainder to check
                if solve(design_local[len(t):]):
                    return True
    # tried all towels, it's not possible
    # save this design so if it comes up again we know not to bother checking.
    cache.append(design_local)
    return False


towels = lines[0].strip().replace(" ", "").split(',')

result = 0
for line in lines[2:]:
    print("trying", line.strip())
    cache = []
    if solve(line.strip()):
        result += 1
print(result)
