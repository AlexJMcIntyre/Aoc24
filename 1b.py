f = open("1_real.txt")
fl = f.readlines()

leftList = []
rightList = []
for line in fl:  # load cards into list
    line = line.strip()
    line = line.split("   ")
    leftList.append(int(line[0]))
    rightList.append(int(line[1]))

leftList.sort()
rightList.sort()

dist = []
for pair in range(len(leftList)):
    dist.append(leftList[pair] * rightList.count(leftList[pair]))

result = sum(dist)
print(result)
