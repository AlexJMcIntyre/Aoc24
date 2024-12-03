file = open("3_real.txt")

instructions = file.read()
instructions = instructions.split("mul")

result = 0
do = 1

for i in instructions:
    process = True

    if i[0] != '(':
        process = False
    end = i.find(')')
    if end == -1:
        process = False
    terms = i[1:end].split(",")
    if len(terms) != 2 or not terms[0].isnumeric() or not terms[1].isnumeric():
        process = False

    if process:
        result += (int(terms[0]) * int(terms[1])) * do

    if "don't()" in i:
        do = 0
    if "do()" in i:
        do = 1

print(result)