import re

with open ("Advent-Of-Code-2022\Day 4\Input.txt",'r') as f:
    lines = f.readlines()
pairs = 0
rangepair= 0
for i in range(len(lines)):
    num = (re.findall(r'\d+', lines[i]))
    num = [int(i) for i in num]
    rangenum = range(num[0],num[1]+1)
    rangenum2 = range(num[2],num[3]+1)
    if (num[0] in rangenum2 and num[1] in rangenum2) or (num[2] in rangenum and num[3]in rangenum):
        rangepair += 1
    
    if (((num[2]) >= (num[0]) and (num[2]) <= (num[1])) and ((num[3]) >= (num[0]) and (num[3]) <= (num[1]))) or (((num[0]) >= (num[2]) and (num[0]) <= (num[3])) and ((num[1]) >= (num[2]) and (num[1]) <= (num[3]))):
        pairs += 1
 
print(pairs)
print(rangepair)