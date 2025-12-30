with open("Day2Input.txt", "r") as file:
    text = file.read().strip()

numbers = []
for v in text.split(","):
    v = v.strip('"')
    start, end = v.split("-")
    numbers.append((int(start), int(end)))

def generate_invalid_ids(max_value):
    max_digits = len(str(max_value))
    invalid = set()

    for L in range(2, max_digits + 1):   # total length of number
        for d in range(1, L // 2 + 1):   # base length
            if L % d != 0:  # if the length of the number has a remainder when divided by repeating sections
                continue

            t = L // d   # number of repeats

            #if part2 and t < 2:
            #    continue

            start = 10**(d - 1)
            end = 10**d - 1

            for base in range(start, end + 1):
                n = int(str(base) * t)
                if n > max_value:
                    break
                invalid.add(n)

    return invalid


def solve_ranges(ranges):

    max_value = max(b for (_, b) in ranges)

    invalid_ids = generate_invalid_ids(max_value)

    total = 0
    for n in invalid_ids:
        for (a, b) in ranges:
            if a <= n <= b:
                total += n
                break

    return total

print("Part 2 =", solve_ranges(numbers))
