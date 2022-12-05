with open ("Day 3\input.txt",'r') as f:
    lines = f.readlines()
compare = []
for i in range(0,len(lines),3):
    line = lines[i]
    lineTwo = lines[i+1]
    lineThree = lines[i+2]
    line = line.strip()
    lineTwo = lineTwo.strip()
    lineThree = lineThree.strip()
    char = ""
    for x in range(len(line)):
        if line[x] in lineTwo and line[x] in lineThree:
            char = line[x]

    compare.append(char)
print(compare)

count = 0
for i in range(len(compare)):
    if compare[i].isupper() == True:
        count += (ord(compare[i]) - 64) + 26
    else:
        count += ord(compare[i]) - 96
print(count)