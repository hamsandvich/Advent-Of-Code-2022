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
elflist.sort(reverse=True)
print(elflist[0]+elflist[1]+elflist[2])