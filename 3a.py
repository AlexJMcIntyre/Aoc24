file = open("3_real.txt")

instructions = file.read()
instructions = instructions.split("mul")

result = 0

for i in instructions:
    if i[0] != '(':
        continue
    end = i.find(')')
    if end == -1:
        continue
    terms = i[1:end].split(",")
    if len(terms) != 2 or not terms[0].isnumeric() or not terms[1].isnumeric():
        continue
    result += (int(terms[0]) * int(terms[1]))

print(result)