import re

with open("AdventOfCodeDay6FormattedValues.txt") as file:
    lines = [re.sub(r"\s+", ",", line.strip()) for line in file]

print(lines)

row = 5          # operator row index
total = 0

# ---- FIXED: get operator characters from the correct row ----
operators = re.findall(r"[+*]", lines[row-1])
columns = len(operators)

for i in range(columns):
    operator = operators[i]       # get the correct operator
    runningTotal = 1

    for ii in range(row-1):
        digit = lines[ii].split(",")
        currentDigit = int(digit[i])

        if operator == "*":
            runningTotal *= currentDigit
        else:  # operator == "+"
            if runningTotal == 1:
                runningTotal += currentDigit - 1
            else:
                runningTotal += currentDigit

    total += runningTotal

print(f"total: {total}")
