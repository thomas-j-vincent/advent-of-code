#!/bin/python3

#import sys
from typing import List

#sys.setrecursionlimit(100000)
#FILE = sys.argv[1] if len(sys.argv) > 1 else "Day6Input.txt"
file = "Day6Input.txt"

def linesToList() -> List[str]:
    lines: List[str] = []
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip("\n")
            # lines.append(list(line)) # Change the return to Line[Line[str]]
            # lines.append([int(v) for v in list(line)])) # Change the signature to List[int]
            lines.append(line)

    return lines

def partTwo():
    lines = linesToList()
    answer = 0

    problems: List[List[int]] = []
    operations = []

    # Alright I'm manually parsing it. First let's scrape the operations.
    operations = lines[-1].split()

    digitLines = lines[:-1]

    lineLength = max(len(l) for l in digitLines)

    problem = []
    for i in range(lineLength):
        value = 0

        allSpaces = True
        for line in digitLines:
            if line[i].isdigit():
                value *= 10
                value += int(line[i])
                allSpaces = False

        if allSpaces:
            problems.append(problem)
            problem = []
        else:
            problem.append(value)
            value = 0

    problems.append(problem)

    for vs, op in zip(problems, operations):
        result = 0

        if op == "*":
            result = 1
            for v in vs:
                result *= int(v)
        else:
            for v in vs:
                result += int(v)

        answer += result

    print(f"Part 2: {answer}")

partTwo()
