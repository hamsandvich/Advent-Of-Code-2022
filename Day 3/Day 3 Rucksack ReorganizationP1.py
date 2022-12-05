with open ("Day 3\input.txt",'r') as f:
    lines = f.readlines()
compare = []
for i in range(len(lines)):
    line = lines[i]
    line = line.strip()
    char = ""
    print(line)
    firsthalf = line[0:len(line)//2]
    secoundhalf = line[len(line)//2:len(line)]
    print(firsthalf)
    print(secoundhalf)
    for x in range(len(firsthalf)):
        for y in range(len(secoundhalf)):
            if firsthalf[x] == secoundhalf[y]:
                char = firsthalf[x]
    compare.append(char)            
print(compare)
count = 0
for i in range(len(compare)):
    if compare[i].isupper() == True:
        count += (ord(compare[i]) - 64) + 26
    else:
        count += ord(compare[i]) - 96
print(count)