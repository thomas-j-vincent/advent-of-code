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

# --- Main Loop ---
for r in range(height):
    for c in range(width):

        if grid[r][c] != "@":
            continue  # skip non-@ cells entirely

        adjacent_cells = getAdjacent(r, c)
        total_at_signs = 0

        # Count '@' in adjacent positions
        for ar, ac in adjacent_cells:
            if grid[ar][ac] == "@":
                total_at_signs += 1

        # Decide accessibility
        if total_at_signs < 4:
            print(f"({r},{c}) ACCESSIBLE")
            row = grid[r]
            grid[r] = row[:c] + "." + row[c+1:]
            total += 1
        else:
            print(f"({r},{c}) NOT ACCESSIBLE")
print(total)