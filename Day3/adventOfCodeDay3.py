with open("AdventOfCodeDay3FormattedValues.txt", "r") as file:
    text = file.read().strip()

text = text.replace("\n", ",")
numbers = [v.strip('"') for v in text.split(",")]

#numbers = [98765431111111,811111111111119,234234234234278, 818181911112111]
total = 0
print(numbers)

for i in numbers:
    number = str(i) #stringified version of the numbers
    length = len(str(i)) #the length of the numbers
    a=0             #resets a as 0
    maxValue = -1
    previousMaxValue = -1
    maxIndex = -1
    minValue = -1

    for index in range(length):
        digit = int(number[index])
        if digit > maxValue:
            previousMaxValue = maxValue
            maxValue = digit
            maxIndex = index

        if (maxIndex+1) == length:
            minValue = maxValue
            maxValue = previousMaxValue

    for index in range(maxIndex + 1, length):
        digit = int(number[index])
        if digit > minValue:
            minValue = digit

    temporaryTotal = (str(maxValue) + str(minValue))
    temporaryTotal = int(temporaryTotal)
    print(temporaryTotal)
    total += temporaryTotal
    print(total)

