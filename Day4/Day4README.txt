Day 3:

Task 1:

DAY 4 TASK 1 DOES NOT CURRENTLY WORK 

In this challenge we had to determine whether a roll of wrapping paper was accessible or not based on whther the spots around it were free or not. The roll
of wrapping paper can only be accessible if there are fewer than four rolls in the adjacent positions. 

My first idea was to loop through the rows one by one as I thought it meant per line but I instead imported the file, reconstructed is as a grid with the 
instructions to find the adjacent cells.This enabled me to iterate through them and find the cells that were accessible or not.

 Explaining the code top to bottom:

We first import the re module, which is used to check whether a string contains a specific character, this would help me to find the character in the list.
The next two lines open the input file, and define the grid as a list of strings (having removed the whitespace and the newline characters) each string is a
row and each character in the string is a cell. This way we can determine both which row a character is (by the list index) and the cells index within the
row (by the strings index).
We then store the height of the grid as the length of "grid" and the width as the length of each string.
"Total", which keeps a running total of the amount of @'s found in a string, is also defined here.

The function getAdjacent gets passed the height and width of the current cell being checked and constucts a list of the other cells around it.
First the function creates a list called "directions" each entry tells the program how to go from the current height and width value
(stored as r and c respectivley). The function then creates the "final" list, this stores the instructions of how to get to an adjacent cell from the current
cell. The "for dr, dc in directions:" loop goes through the values in the directions and for each one adds the row value i.e. 3 with the instruction cell
index i.e. -2. To get a useable position. The if statement is designed in the case that the cell being checked is near the edge or top of the grid, and if
it isn't, it appends it to the "final" list
This "final" list is then returned.

The main loop loops through both the height and width (cell by cell) and if the cell isnt an @ skips it. (as there is no paper to check if accessible)
"adjactentCells" calls the function "getAdjacent" to return a list of all the cells adjacent to the current one that need to check if they are free or not.
"totalAtSigns" is a running total of taken cells, if this reaches four or above the roll is deemed inaccessible. This is defined here out of the for loop.
The "for ar, ac in adjacentCells:" loop loops through all the available adjacent cells, checking if they contain @ and if they do it adds one to the
totalAtSigns. There is then a final is statement and if the totalAtSigns is less than 4 it replaces the @ sign with a . (simulating removal of that roll)
and then it increments the total.
The total is then printed.

Maximising efficiency:

To maximise the efficiency all I could do is remove the re module as it wan't used in the end.

Task 2: 

In task two we have to loop the program, removing all prossible rolls of wrapping paper, counting the number we remove, substituting it for a . to simulate
removing it, and then rerunning the program with the new grid.

 Explaining the code top to bottom:

The function "get_adjacent_positions" works in a similar way to the function from the first function, getting passed:
"r" (height index), "c" (width index) as well as the actual height and the width of the grid. The function starts by declaring the "positions" list, this is
where the indexes of the adjacent positions will be appended. The for loops go through the 8 adjacent positions (two for loops, one for x, one for y value)
The if statement ensures that the centre cell is skipped, as this cell is not adjacent. "nr" and "nc" are then given the value of the adjacent character
with the line "nr, nc = r + dr, c + dc". The if statement ensures that the adjacent value is a valid value before appending the value to the postions list.
positions is then returned.  

We then open the file the same was as in the first program however, this time we write to list using the list function which converts the input into a list
directly. "height", "width", and "total_removed" are declared in the same way as in the first program. The "while: TRUE" intentionally loops until
"to_remove" is empty


