file = open("5_real.txt")
lines = file.readlines()


class Rule:
    def __init__(self, local_line):
        self.v1, self.v2 = local_line.strip().split("|")


class Update:
    def __init__(self, local_line):
        self.page_list = local_line.strip().split(",")

    def check(self):
        for page_number in range(1, len(self.page_list)):  # skip the zeroth since nothing can come before it.
            page = self.page_list[page_number]
            # find rules that mention page as first term
            for rule in rule_list:
                if page == rule.v1:
                    # there is a rule saying v2 cannot come before this page, check
                    if rule.v2 in self.page_list[0:page_number]:
                        # v2 comes before, fail this check
                        return False
        # all checks passed,
        return True


rule_list = []
update_list = []

for line in lines:
    if "|" in line:
        rule_list.append(Rule(line))
    if "," in line:
        update_list.append(Update(line))

results = []

for u in update_list:
    if u.check():
        results.append(int(u.page_list[int(len(u.page_list)/2)]))

print(sum(results))
