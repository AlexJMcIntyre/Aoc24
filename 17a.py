import math

file = open("17_real.txt")
lines = file.readlines()

A = int(lines[0].split(":")[1].strip())
B = int(lines[1].split(":")[1].strip())
C = int(lines[2].split(":")[1].strip())
P = [int(p) for p in lines[4].split(":")[1].strip().split(",")]
i = 0
output = ''


def combo(operand):
    global A
    global B
    global C
    if 0 <= operand <= 3:
        return operand
    elif operand == 4:
        return A
    elif operand == 5:
        return B
    elif operand == 6:
        return C


def inst(opcode, operand):
    global A
    global B
    global C
    global i
    global output
    if opcode == 0:
        # adv
        A = math.trunc(A / (2 ** combo(operand)))
        i += 2
    elif opcode == 1:
        # bxl
        B = B ^ operand
        i += 2
    elif opcode == 2:
        # bst
        B = combo(operand) % 8
        i += 2
    elif opcode == 3:
        # jnz
        if A != 0:
            i = operand
        else:
            i += 2
    elif opcode == 4:
        # bxc
        B = B ^ C
        i += 2
    elif opcode == 5:
        # out
        output = output + str(combo(operand) % 8) + ','
        i += 2
    elif opcode == 6:
        # bdv
        B = int(A / (2 ** combo(operand)))
        i += 2
    elif opcode == 7:
        # cdv
        C = int(A / (2 ** combo(operand)))
        i += 2


while i < len(P):
    inst(P[i], P[i+1])

print(output[:-1])

