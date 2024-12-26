file = open("22_real.txt")
lines = file.readlines()


def next_secret(l_secret, l_list):
    def prune(lf_secret):
        return lf_secret % 16777216

    def mix(lf_value, lf_secret):
        return lf_value ^ lf_secret

    def step1(lf_secret):
        return prune(mix(lf_secret * 64, lf_secret))

    def step2(lf_secret):
        return prune(mix(int(lf_secret / 32), lf_secret))

    def step3(lf_secret):
        return prune(mix(lf_secret * 2048, lf_secret))

    ns = step3(step2(step1(l_secret)))
    l_list.append(ns)
    return ns


all_dict = {}
for line in lines:
    secret = int(line.strip())
    monkey_list = [secret, ]

    for i in range(2000):
        secret = next_secret(secret, monkey_list)
    monkey_dict = []
    for i in range(4, 2001):
        seq = (monkey_list[i - 3] % 10 - monkey_list[i - 4] % 10,
               monkey_list[i - 2] % 10 - monkey_list[i - 3] % 10,
               monkey_list[i - 1] % 10 - monkey_list[i - 2] % 10,
               monkey_list[i] % 10 - monkey_list[i - 1] % 10)
        price = monkey_list[i] % 10
        if seq not in monkey_dict:
            monkey_dict.append(seq)
            if seq in all_dict:
                all_dict[seq] += price
            else:
                all_dict[seq] = price

best = (max(all_dict, key=all_dict.get))
print(best)
print(all_dict[best])
