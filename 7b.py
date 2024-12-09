import math
from itertools import product

file = open("7_real.txt")
lines = file.readlines()


class Equation:
    def __init__(self, local_line):
        self.test_value = int(local_line.strip().split(":")[0])
        self.terms = [int(x) for x in local_line.strip().split(":")[1].split()]

    def term_test(self):
        operations = ['+', '*', '||']
        # operator count is one less than terms
        op_list = list(product(operations, repeat=len(self.terms)-1))
        for order in op_list:
            total = self.terms[0]
            for op in enumerate(order):
                if op[1] == '+':
                    total += self.terms[op[0]+1]
                elif op[1] == '*':
                    total = total * self.terms[op[0]+1]
                elif op[1] == '||':
                    total = int(str(total) + str(self.terms[op[0]+1]))
            if total == self.test_value:
                return True
        # tried all orders, none worked.
        return False


eq_list = []
for line in lines:
    eq_list.append(Equation(line))

results = 0
for eq in eq_list:
    if eq.term_test():
        results += eq.test_value

print(results)
