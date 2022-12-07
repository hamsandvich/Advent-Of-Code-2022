with open ("Advent-Of-Code-2022\Day 6\input.txt",'r') as f:
    lines = f.readlines()
lines = lines[0]
fourchar = []
charcount = 0
for i in range(len(lines)):
    charcount += 1
    fourchar.append(lines[i])
    setofchar = set(fourchar)
    if len(setofchar) == 14:
        break
    if len(fourchar) == 14:
        fourchar.pop(0)
print(charcount)
