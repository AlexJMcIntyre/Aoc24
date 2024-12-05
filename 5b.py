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


def check_pair(a, b):  # checks if a needs to go before b
    for rule in rule_list:
        if a == rule.v1 and b == rule.v2:
            return True
    return False


def fit_single(single, current_list):  # adds a single element into a possibly-empty list in the correct order
    if current_list:  # the current list is not empty
        # check against each element of the current list to see if it needs to go before any existing term:
        for element in enumerate(current_list):
            if check_pair(single, element[1]):
                # single needs to go before element[0]
                current_list.insert(element[0], single)
                return current_list
        # we've checked all existing elements, so it can be inserted at the end
        current_list.append(single)
        return current_list
    else:  # the current list *is* empty
        current_list.append(single)
        return current_list


def reorder(current_list):
    local_output = []
    while current_list:
        single = current_list.pop(0)
        local_output = fit_single(single, local_output)
    return local_output


rule_list = []
update_list = []

for line in lines:
    if "|" in line:
        rule_list.append(Rule(line))
    if "," in line:
        update_list.append(Update(line))

results = []

for u in update_list:
    if not u.check():
        output = reorder(u.page_list)
        results.append(int(output[int(len(output)/2)]))

print(sum(results))
