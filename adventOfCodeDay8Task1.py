import re

lines = open("Input.txt").readlines()
print(lines)
p1_total = 0
for line in lines:
    p1_total += 2
    p1_total += len(re.findall("\\\[\"\\\]", line))
    p1_total += 3 * len(re.findall("\\\[x][0-9a-f]{2}", line))
    print(p1_total)
print(p1_total )

p2_total = 0
for line in lines:
    p2_total +=4
    p2_total += 2 * len(re.findall("\\\[\"\\\]", line))
    p2_total += len(re.findall("\\\[x][0-9a-f]{2}", line))
print(p2_total)