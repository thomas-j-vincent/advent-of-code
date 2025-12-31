def get_adjacent_positions(r, c, height, width):
    positions = []
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < height and 0 <= nc < width:
                positions.append((nr, nc))
    return positions


with open("Day4Input.txt") as f:
    grid = [list(line.strip()) for line in f]

height = len(grid)
width = len(grid[0])

total_removed = 0

while True:
    to_remove = []

    # 1. Find all accessible @
    for r in range(height):
        for c in range(width):
            if grid[r][c] != "@":
                continue

            adj = get_adjacent_positions(r, c, height, width)
            count_adjacent_at = sum(1 for (ar, ac) in adj if grid[ar][ac] == "@")

            if count_adjacent_at < 4:
                to_remove.append((r, c))

    # 2. Stop if none found
    if not to_remove:
        break

    # 3. Remove them all
    for (r, c) in to_remove:
        grid[r][c] = "."
        total_removed += 1

print("TOTAL REMOVED:", total_removed)
