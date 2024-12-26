file = open("22_real.txt")
lines = file.readlines()


def next_secret(l_secret):
    def prune(lf_secret):
        return lf_secret % 16777216

    def mix(lf_value, lf_secret):
        return lf_value ^ lf_secret

    def step1(lf_secret):
        return prune(mix(lf_secret * 64, lf_secret))

    def step2(lf_secret):
        return prune(mix(int(lf_secret/32), lf_secret))

    def step3(lf_secret):
        return prune(mix(lf_secret * 2048, lf_secret))

    return step3(step2(step1(l_secret)))


result = 0
for line in lines:
    secret = int(line.strip())
    for i in range(2000):
        secret = next_secret(secret)
    result += secret

print(result)
