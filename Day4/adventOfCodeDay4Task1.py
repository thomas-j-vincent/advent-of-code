import re
with open("AdventOfCodeDay4FormattedValues.txt", "r") as file:
    lines = {index: line.strip() for index, line in enumerate(file, start=1)}
    # print(lines[137]) 137 x 137lines of grid
    gridLength = len(lines) + 1

    def getAdjacent(atLine, value):
        adjacent = {
        "blLine": (atLine -1, value -1),
        "bcLine": (atLine -1, value),
        "brLine": (atLine +1, value +1),
        "clLine": (atLine, value -1),
        "crLine": (atLine, value +1),
        "flLine": (atLine +1, value -1), 
        "fcLine": (atLine +1, value),
        "frLine": (atLine +1, value +1)
        }
        return adjacent

    for index in range(gridLength):
        #atLine = index +1
        atLine = 1 +1 # TESTING
        for rowLength in range(gridLength):
            atRow = rowLength +1 # presuming rowlength acts like gridlengthand subtracts one
            #atRow = 1 +1 # TESTING
            total = 0
            at = getAdjacent(atLine, atRow)
            blcolumn = at["blLine"][0] #gets the column value from the adjacent function
            blrow = at["blLine"][1]    #gets the row value from the adjacent function (0 is selecting the digit, not important)
            bccolumn = at["bcLine"][0] 
            bcrow = at["bcLine"][1]   
            brcolumn = at["brLine"][0] 
            brrow = at["brLine"][1]    
            clcolumn = at["clLine"][0] 
            clrow = at["clLine"][1]   
            crcolumn = at["crLine"][0] 
            crrow = at["crLine"][1]    
            flcolumn = at["flLine"][0] 
            flrow = at["flLine"][1] 
            frcolumn = at["frLine"][0] 
            frrow = at["frLine"][1]    
                #print(lines[1][24]) # prints the line at that column, row
            print(lines[blcolumn][blrow])
            txt = lines[blcolumn][blrow]
            search = re.search("@",txt )
            if search:
                print("yup")
                total += 1
            else: print("no")
    
            txt = lines[bccolumn][bcrow]
            search = re.search("@",txt )
            if search:
                print("yup")
                total += 1
            else: print("no")
    # ---------------------------------------------------
            txt = lines[brcolumn][brrow]
            search = re.search("@",txt )
            if search:
                print("yup")
                total += 1
            else: print("no")
    
            txt = lines[clcolumn][clrow]
            search = re.search("@",txt )
            if search:
                print("yup")
                total += 1
            else: print("no")
    
            txt = lines[crcolumn][crrow]
            search = re.search("@",txt )
            if search:
                print("yup")
                total += 1
            else: print("no")
    
            txt = lines[flcolumn][flrow]
            search = re.search("@",txt )
            if search:
                print("yup")
                total += 1
            else: print("no")
    
            txt = lines[flcolumn][flrow]
            search = re.search("@",txt )
            if search:
                print("yup")
                total += 1
            else: print("no")
    
            txt = lines[flcolumn][flrow]
            search = re.search("@",txt )
            if search:
                print("yup")
                total += 1
            else: print("no")
    
            if total < 4:
                print("ACCESSIBLE")
            else: 
                print("NOT ACCESSIBLE")
        #    bL 
 #   bC
  #  bR
   # cL    
   # cC = number[index]
   # cR
   # fL
   # fC
   # fR