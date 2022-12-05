## 

with open ("Advent-Of-Code-2022\Day 1\input.txt",'r') as f:
    lines = f.readlines()

print(lines)
elflist = []
calories = 0
elf = "elf #"
elfnum = 1
for i in range(len(lines)):
    line = lines[i]
    line = line.split('\n')

    if len(line[0]) < 1:
        print(elf + str(elfnum) + " has " + str(calories) + " calories")
        elflist.append(calories)
        calories = 0
        elfnum += 1
    else:
        calories += int(line[0])
print(elf + str(elfnum) + " has " + str(calories) + " calories")
elflist.append(calories)
max = 0
for i in range(len(elflist)):
    if int(elflist[i]) > max:
        max = int(elflist[i])
        index = i
print("Elf #" + str(index + 1) + " has the most calories with " + str(max) + " calories")
