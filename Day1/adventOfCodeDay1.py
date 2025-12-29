# import numbers
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
        txtB = f" isZero, occurences: {zeroOccurences}"
        print(txtB)
        #print(f" isZero, occurences: {zeroOccurences}")
    return(zeroOccurences)

def isMaxOrMin(currentValue, zeroOccurences):
    while currentValue > 99 or 0 > currentValue :
        if currentValue > 99: #if currentValue > 99
            currentValue = (currentValue - 100)# -99 (-100)
        elif currentValue < 0: #if currentValue < 0
            currentValue = (currentValue + 100)# +99 (+100)

    return currentValue, zeroOccurences

#for numbers
for i in numbers:
    if i[0] == "L":  # if first digit is l - the number
        value = (i[1:]) #slices value into just the numbers
        value = int(value)      #converts to int
        currentValue -= value # subtracts value from current value
    
    elif i[0] == "R":  # else if first digit is r add the number
        value = (i[1:])   #slices just the numbers
        value = int(value)         #convert to int
        currentValue += value  #adds value to current value

    currentValue, zeroOccurences = isMaxOrMin(currentValue, zeroOccurences)
    zeroOccurences = isZero(currentValue, zeroOccurences)