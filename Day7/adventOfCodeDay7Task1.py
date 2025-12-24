import re
with open("AdventOfCodeDay7FormattedValues.txt", "r") as f:
    lines = [line.strip() for line in f]

txt=(lines[0])
#print(txt)
x=re.search("S",txt)
txt = str([x.span()[0]])
txt= int(txt.strip("[]")) #the column containing s

for i in range(1, len(lines)): #loops through the lines
    value = lines[i]  # prints a line
   # print(i) # prints a column
    index = 0 # index of the ii loop
    if value[txt] == ".":
        row = list(value)        # convert string → list
        row[txt] = "|"           # replace the . with |
     #   print(lines[i])
    elif value[txt] == "^":
        row = list(value)
        if txt-1 >=0:
            row[txt - 1] = "|"
        row[txt]

        if txt+1 < len(row):
            row[txt+1] = "|"

    lines[i] = "".join(row)
    print(lines[i])

    for ii in lines[i]: #ii is the character value not the index of that character
        index += len(ii)
    #    print(index)
        #previousRow = i-1
        #character = str(lines[i][int(ii)])
        #print(character)
        #if lines[previousRow][ii] == "|":
         #   print("lineabove")
