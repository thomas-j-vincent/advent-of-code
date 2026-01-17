# Day 9

## Task 1: ##

On Day 9 we find ourselves in a movie theatre! Here, the elves are decorating by replacing some of the square floor tiles for red ones. The elves want us to find the largest rectangle that uses red tiles for two of the opposite corners. The puzzle input is a list of where the red tiles are located in the grid.

 ### Explaining the code top to bottom:###

First we define day 9 as a class, this groups all of the variables and means that we do not have to use global variables.

You can access these variables and functions using "self" when calling the function and "self." when creating variables. 

The `` __init__(self):`` function runs automatically when we create the day9 object, this function creates the ```self.coords``` (stores coordinate pairs) and ```self.max_area``` (stores the largest area found) variables.

The ``def open_and_store(self):`` function is used to open the data from the input file, reading the coordinate pairs by row, replacing the newline characters with blankspace. It then turns each of these values into integers so they can be treated as numbers rather than strings.

``def calc_area(self,a,b):``

