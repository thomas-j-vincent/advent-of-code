import re
with open("AdventOfCodeDay6FormattedValues.txt") as file:
    # lines = [line.strip().replace(" ", ",") for line in file]  #each line is a entry in a list: ["12 1 2 3 4 5 3 45", "2 4 5 98 34"]
    lines = [re.sub(r"\s+", ",", line.strip()) for line in file]
    #lines = ["123,328,51,64"," 45,64,387,23","6,98,215,314","*,+,*,+"]
    #print(lines)
    line = str(lines)
    row = 5
    #row = 4 #TESTSSSSEEEEEEEERRRR
    addition = re.findall(r"[+*]", line)
    columns = len(addition)
    # lines is 5 long
    # a value is accessed by quoting lines[1-4]then the index within that line
    total = 0
    #lines = 
    for i in range(columns): # in every column (1000)
        parts = lines[row-1].split(",")#[int(index)]
        operator =parts[i] #operator.replace(",", "")
        runningTotal = 1
        #operator.strip(" ")
        #print(operator)

        for ii in range(row-1):
            digit = (lines[ii].split(","))
            currentDigit = digit[i]
            currentDigit= int(currentDigit)
            print(currentDigit)
           # print(digit[ii])
           # print(f"pre:{runningTotal}")
            if operator == "*":
                runningTotal = currentDigit * runningTotal
            #    print(f"*:{runningTotal}")
            elif operator == "+":
                if runningTotal == 1:
                    runningTotal = (currentDigit + runningTotal)-1
             #       print(f"=1{runningTotal}")
                else:
                    runningTotal = currentDigit + runningTotal
                    print(f"+{runningTotal}")
        
        total = runningTotal + total
        print(f"total:{total}")

    print(f"total:{total}")
      #      previousDigit = (lines[row-1].split(","))
            
    #    print(result)
