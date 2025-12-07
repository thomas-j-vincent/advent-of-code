# import numbers
with open("FormattedValues.txt", "r") as file:
    text = file.read().strip()

# Example list. Replace with: numbers = text.split(",")
#numbers = ["L68","L30","R48","L5","R60","L55","L1","L99","R14","L82"]
numbers = [v.strip('"') for v in text.split(",")]

currentValue = 50
zeroOccurences = 0


# === Helper Functions ===

def isZero(currentValue, zeroOccurences):
    """Counts whenever the number lands exactly on 0."""
    if currentValue == 0:
        zeroOccurences += 1
        #print(f"Hit ZERO! Total zero crossings: {zeroOccurences}")
    return zeroOccurences


def applyMovement(currentValue, movement, zeroOccurences):
    """
    Moves one step at a time, wrapping correctly, and counting zero crossings.
    Example:
       movement = -68 → move left (decrease) 68 times.
    """
    step = 1 if movement > 0 else -1

    for _ in range(abs(movement)):
        currentValue += step

        # Wrap around behaviour
        if currentValue > 99:
            currentValue = 0
        elif currentValue < 0:
            currentValue = 99

        zeroOccurences = isZero(currentValue, zeroOccurences)

    return currentValue, zeroOccurences


# === MAIN LOOP ===

for instr in numbers:
    direction = instr[0]
    value = int(instr[1:])

    movement = -value if direction == "L" else value

    #print(f"\nInstruction: {instr}")
    #print(f"Moving {'LEFT' if movement < 0 else 'RIGHT'} by {abs(movement)}")

    currentValue, zeroOccurences = applyMovement(currentValue, movement, zeroOccurences)

    #print(f"Position after move: {currentValue}")


print("\n================================")
print("FINAL ZERO CROSSINGS:", zeroOccurences)
print("================================")