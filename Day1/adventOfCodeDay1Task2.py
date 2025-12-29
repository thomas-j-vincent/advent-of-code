values = []

with open("Day1Input.txt", "r") as file:
    for line in file: # read file line by line
        values.append(line.strip())

    formatted = ",".join(f'"{v}"' for v in values) # format file

numbers = [v.strip('"') for v in formatted.split(",")]
#numbers = ["L68","L30","R48","L5","R60","L55","L1","L99","R14","L82"]
currentValue = 50
zeroOccurences = 0

def isZero(currentValue, zeroOccurences):
    if currentValue == 0:     #if number equals 0 
        zeroOccurences += 1     # add one to 0 occurences
    return(zeroOccurences)

def isMaxOrMin(currentValue,movement, zeroOccurences):

    step = 1 if movement > 0 else -1

    for i in range(abs(movement)): #abs takes out the + or - sign
        currentValue += step
        if currentValue > 99: #if currentValue > 99
            currentValue = (currentValue - 100)# -99 (-100)
        elif currentValue < 0: #if currentValue < 0
            currentValue = (currentValue + 100)# +99 (+100)

        zeroOccurences = isZero(currentValue, zeroOccurences)

    return currentValue, zeroOccurences

for i in numbers:
    direction = i[0]
    value = int(i[1:])

    movement = -value if direction == "L" else value
    currentValue, zeroOccurences = isMaxOrMin(currentValue,movement, zeroOccurences)


print(zeroOccurences)