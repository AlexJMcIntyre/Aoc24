file = open("19_real.txt")
lines = file.readlines()


def solve(design):
    cache = {}

    def check_frag(right):
        ways = 0
        if right == '':
            return 1
        if right in cache:
            return cache[right]
        towels_to_check = [t for t in towels if t in right]
        for t in towels_to_check:
            if t == right[:len(t)]:
                ways += check_frag(right[len(t):])
        cache[right] = ways
        return ways

    return check_frag(design)


towels = lines[0].strip().replace(" ", "").split(',')

result = []
for line in lines[2:]:
    print("trying", line.strip())
    score = solve(line.strip())
    result.append(score)
print(result)
print(sum(result))
