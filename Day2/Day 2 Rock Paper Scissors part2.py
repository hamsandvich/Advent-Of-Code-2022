
with open ("Advent-Of-Code-2022\Day2\input.txt",'r') as f:
    lines = f.readlines()

# We have a for rock B for paper and C for scissors
# we have x for rock y for paper and z for scissors

score = 0

for i in range(len(lines)):
    line = lines[i]
    line = line.split('\n')
    print(line)
    if line[0][0] == "A":
        if line[0][2] == "X":
            score += 3
        elif line[0][2] == "Y":
            score += 4
        elif line[0][2] == "Z":
            score += 8
    elif line[0][0] == "B":
        if line[0][2] == "X":
            score += 1
        elif line[0][2] == "Y":
            score += 5
        elif line[0][2] == "Z":
            score += 9
    elif line[0][0] == "C":
        if line[0][2] == "X":
            score += 2
        elif line[0][2] == "Y":
            score += 6
        elif line[0][2] == "Z":
            score += 7
print(score)