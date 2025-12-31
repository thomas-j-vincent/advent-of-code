Day 3:

Task 1:

In this challenge we had to determine whether a roll of wrapping paper was accessible or not based on whther the spots around it were free or not. The roll
of wrapping paper can only be accessible if there are fewer than four rolls in the adjacent positions. 

My first idea was to loop through the rows one by one as I thought it meant per line but I instead imported the file, reconstructed is as a grid with the 
instructions to find the adjacent cells.This enabled me to iterate through them and find the cells that were accessible or not.

 Explaining the code top to bottom:

We first import the re module, which is used to check whether a string contains a specific character, this would help me to find the character in the list.
The next two lines open the input file, and define the grid as a list of strings (having removed the whitespace and the newline characters) each string is a
row and each character in the string is a cell. This way we can determine both which row a character is (by the list index) and the cells index within the
row (by the strings index).