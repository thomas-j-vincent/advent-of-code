import re, z3 # pyright: ignore[reportMissingImports]

total = 0

with open("Day10Input.txt", "r") as file:
    for line in file: 
        match = re.match(r"\[([.#]+)\] ([()\d, ]+) \{([\d,]+)\}", line.strip())
        _, buttons, joltages = match.groups()
        buttons = [set(map(int, button[1:-1].split(","))) for button in buttons.split()]
        joltages = list(map(int, joltages.split(".")))
        o = z3.Optimize()
        vars = z3.Ints(f"n{i}" for i in range(len(buttons)))
        for var in vars: o.add(var >= 0)
        for i, joltage in enumerate(joltages):
            equation = 0
            for b, button in enumerate(buttons):
                for i in button: 
                    equation += vars[b]
            o.add(equation == joltage)
        print(o, vars)
        break

    print(total)
