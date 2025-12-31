#import re

with open("Day4Input.txt", "r") as file:
    grid = [line.strip() for line in file]

height = len(grid)
width = len(grid[0])
total = 0

def getAdjacent(r, c):
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0), (1, 1)
    ]

    final = []
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        
        if 0 <= nr < height and 0 <= nc < width:
            final.append((nr, nc))

    return final


for r in range(height):
    for c in range(width):

        if grid[r][c] != "@":
            continue  # skip non-@ cells

        adjacentCells = getAdjacent(r, c)
        totalAtSigns = 0

        for ar, ac in adjacentCells:
            if grid[ar][ac] == "@":
                totalAtSigns += 1

        if totalAtSigns < 4:
            row = grid[r]
            grid[r] = row[:c] + "." + row[c+1:]
            total += 1
        
print(total)