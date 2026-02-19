# Day 12

## Task 1: ##

There's only one task for this day as the second star is awarded as a result of completing all previous challenges. For this challenge we first had to fit presents of differing sizes into different matrixes. In the first part of the input the shapes of the presents are listed, where a has # marks a filled space and a . marks an empty shape, there are 5 of these different shapes. In the second part of the input the sizes of the matrixes are listed, ie the first one is: 47x49, seperated by the colon is the number of each shape expected to fit into the matrix. so that 60 48 64 49 52 78 means that 60 shape ones, 48 shape two's, 64 shape three's etc. are supposed to fit. You only count the regions that fit all the presents.

 ### Explaining the code top to bottom:###

In the first line we import the re module so that we can use re.findall and map in the code, we then open the input and split lines at the newline character. Total is then set at 0, outside all loops so it doesn't get reset accidentally.
For each line we search for all numbers, returning them as a string (they get converted into an integer later), the first two of these numbers are then mapped to the variables x and y, and all the others are returned to counts as a list. 
If x//3 * y//3 is greater than or equal to the sum of counts we know there will be enough space for all of the presents, therefore we add one to the total and repeat the loop.
The total is then printed.

  ### Maximising efficiency: ###

This code is very minimalist and therefore isn't anything we can do to make it more efficient