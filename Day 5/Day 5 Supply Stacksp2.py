import re

with open ("Advent-Of-Code-2022\Day 5\input.txt",'r') as f:
    lines = f.readlines()
    
creane = lines[0:9]
print(creane)
lines = lines[10:]
lines = [line.strip() for line in lines]

one = []
two = []
three = []
four = []
five = []
six = []
seven = []
eight = []
nine = []

for i in range(8,-1,-1):
    for j in range(len(creane[i])):
        if creane[i][j].isalpha() and j == 1:
            one.append(creane[i][j])
        elif creane[i][j].isalpha() and j == 5:
            two.append(creane[i][j])
        elif creane[i][j].isalpha() and j == 9:
            three.append(creane[i][j])
        elif creane[i][j].isalpha() and j == 13:
            four.append(creane[i][j])
        elif creane[i][j].isalpha() and j == 17:
            five.append(creane[i][j])
        elif creane[i][j].isalpha() and j == 21:
            six.append(creane[i][j])
        elif creane[i][j].isalpha() and j == 25:
            seven.append(creane[i][j])
        elif creane[i][j].isalpha() and j == 29:
            eight.append(creane[i][j])
        elif creane[i][j].isalpha() and j == 33:
            nine.append(creane[i][j])
assembledStack = {1:one,2:two,3:three,4:four,5:five,6:six,7:seven,8:eight,9:nine}

for i in range(len(lines)):
    num = (re.findall(r'\d+', lines[i]))
    num = [int(i) for i in num]
    numberOfCrates = num[0]
    stacknumber = num[1]
    stacknumber2 = num[2]
    for i in range(numberOfCrates):
        assembledStack[stacknumber2].append(assembledStack[stacknumber].pop(-numberOfCrates))
        numberOfCrates -= 1

for i in range(1,10):
    print(assembledStack[i].pop())