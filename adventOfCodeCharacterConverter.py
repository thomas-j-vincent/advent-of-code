
values = []

with open("AdventOfCodeDay1Values.txt", "r") as file:  # open text file
    for line in file: # read file line by line
        values.append(line.strip())

formatted = ",".join(f'"{v}"' for v in values) # format file

with open("AdventOfCodeDayFormattedValues.txt", "w") as output_file:
    output_file.write(formatted)

print("Saved to FormattedValues.txt")

# save file
# close file