with open("Day3Input.txt", "r") as file:
    text = file.read().strip()

text = text.replace("\n", ",")
numbers = [v.strip('"') for v in text.split(",")]
#numbers = [98765431111111,811111111111119,234234234234278, 818181911112111]
total = 0

for i in numbers:
   # number = str(i) #stringified version of the numbers
    #length = 100 #len(str(i)) #the length of the numbers
    maxValue = -1
    previousMaxValue = -1
    maxIndex = -1
    minValue = -1

    for index, digit_char in enumerate(str(i)):
        digit = int(digit_char)
        if digit > maxValue:
            previousMaxValue = maxValue
            maxValue = digit
            maxIndex = index

        if (maxIndex+1) == 100:
            minValue = maxValue
            maxValue = previousMaxValue

    for index, digit_char in enumerate(str(i)):
        if index > maxIndex:
            digit = int(digit_char)
            if digit > minValue:
                minValue = digit

    temporaryTotal = int(str(maxValue) + str(minValue))
    #temporaryTotal = int(temporaryTotal)
    total += temporaryTotal
    print(total)

