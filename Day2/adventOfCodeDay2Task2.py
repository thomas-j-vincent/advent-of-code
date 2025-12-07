import re
# import numbers
with open("AdventOfCodeDay2FormattedValues.txt", "r") as file:
    text = file.read().strip()

ranges = [v.strip('"') for v in text.split(",")]
def generate_invalid_ids(max_value, part2=False):
    """
    Generates all invalid IDs up to max_value.
    Part 1: only repeated twice (t = 2)
    Part 2: repeated at least twice (t >= 2)
    """
    max_digits = len(str(max_value))
    invalid = set()

    for L in range(2, max_digits + 1):   # total length of number
        for d in range(1, L // 2 + 1):   # base length
            if L % d != 0:
                continue

            t = L // d   # number of repeats

            # Part 1 requires exactly 2 repeats, Part 2 requires ≥2
            if not part2 and t != 2:
                continue
            if part2 and t < 2:
                continue

            start = 10**(d - 1)
            end = 10**d - 1

            for base in range(start, end + 1):
                n = int(str(base) * t)
                if n > max_value:
                    break
                invalid.add(n)

    return invalid


def solve_ranges(ranges, part2=False):
    """
    Returns the sum of all invalid IDs inside the given ranges.
    ranges = list of (start, end)
    """
    max_value = max(b for (_, b) in ranges)

    invalid_ids = generate_invalid_ids(max_value, part2=part2)

    total = 0
    for n in invalid_ids:
        for (a, b) in ranges:
            if a <= n <= b:
                total += n
                break

    return total


print("Part 1 =", solve_ranges(ranges, part2=False))


print("Part 2 =", solve_ranges(ranges, part2=True))
