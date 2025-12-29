with open("Day2Input.txt", "r") as file:
    text = file.read().strip()

numbers = [v.strip('"') for v in text.split(",")]
#numbers = ["11-22","95-115","998-1012","1188511880-1188511890","222220-222224",
#"1698522-1698528","446443-446449","38593856-38593862","565653-565659",
#"824824821-824824827","2121212118-2121212124"]

total = 0

#def check_odd_even(num, a):
#    if num % a == 0:
#        return "Even"
#    else:
#        return "Odd"

for i in numbers:
    start, end = i.split("-")       # split into "11", "22"
    start, end = int(start), int(end)

    for value in range(start, end + 1):
        a = len(str(value))
        if a % 2 != 0:  #only accept numbers with even amounts of digits
            continue
    #    if a == 2:
     #       if value % 11 == 0: # between 11- 99 it can only be dividisable by 11
      #          total += value
       #         continue
          #  else: 
           #     total += value
            #    continue

    #    b = (a / 2) # take number of digits, half it.
     #   b = int(b) # b needs to become two sets of b where value is 1 ie b = 2 needs to be 11   11
      #  ones = "1" * b 
#        modified = ones[0] + "0" * (len(ones) - 1) #replace first digit with 1 and the rest 0
 #       final = modified + modified 
  #      final = int(final) # this is the lowest acceptable number for that amount of digits
   #     nines = "9" * a   # take number of digits replace all with 9
    #    nines = int(nines)# that is the highest acceptable number for that amount of digits
        #if value > nines or value < final:
        #    continue
        #else:
        value = str(value)
        split = len(value) // 2# take number of digits, half it.
        left = value[:split]
        right = value[split:]
        #i = 0
        allMatch = True
        
        for ii in range(split):
            if left[ii] != right[ii]:
                allMatch = False
                break

        if allMatch:
               # reassembled = left + right
               # reassembled = int(reassembled)
            total += int(value)

txtB = f" total: {total}"
print(txtB)






# look for patterns that are half as many digits long as the whole number is 
# sperate number into two numbers of equal length ie. 2222 = 22, 22 
# compare first digit of each number- if equal continue. otherwise discard
# compare second number, if equal continue, otherwise discard. 
# continue for length of number
# if it passes, add to counter 