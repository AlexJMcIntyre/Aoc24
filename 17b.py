import math

file = open("17_real.txt")
lines = file.readlines()

Ao = int(lines[0].split(":")[1].strip())
Bo = int(lines[1].split(":")[1].strip())
Co = int(lines[2].split(":")[1].strip())
Po = [int(p) for p in lines[4].split(":")[1].strip().split(",")]

A = Ao
B = Bo
C = Co
P = Po.copy()
output = ''

output_check = ''
for x in P:
    output_check = output_check + str(x) + ','


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


i = 0
      #  3064165110264632
      #  3004165110264632
A = int('3004165110264632', 8)
print(A)


while i < len(P):
    inst(P[i], P[i + 1])
print(output)
print(output_check)

checklist = ''
for i in range(16):
    if output[2*i] == output_check[2*i]:
        checklist += '#,'
    else:
        checklist += '-,'
print(checklist)


# for j in range(1000000):
#     B = Bo
#     C = Co
#     P = Po.copy()
#     A = j
#     i = 0
#     output = ''
#     while i < len(P):
#         inst(P[i], P[i+1])
#     results.append((j, output))
#     if output == output_check:
#         print(j)
#         break
#
# with open('17_output.csv', 'w') as file:
#     for line in results:
#         file.write(str(line))
#         file.write('\n')
