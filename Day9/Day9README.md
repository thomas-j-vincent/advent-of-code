# Day 9

## Task 1: ##

On Day 9 we find ourselves in a movie theatre! Here, the elves are decorating by replacing some of the square floor tiles for red ones. The elves want us to find the largest rectangle that uses red tiles for two of the opposite corners. The puzzle input is a list of where the red tiles are located in the grid.

 ### Explaining the code top to bottom:###

First we define day 9 as a class, this groups all of the variables and means that we do not have to use global variables.

You can access these variables and functions using "self" when calling the function and "self." when creating variables. 

The `` __init__(self):`` function runs automatically when we create the day9 object, this function creates the ```self.coords``` (stores coordinate pairs) and ```self.max_area``` (stores the largest area found) variables.

The ``def open_and_store(self):`` function is used to open the data from the input file, reading the coordinate pairs by row, replacing the newline characters with blankspace. It then turns each of these values into integers so they can be treated as numbers rather than strings.

``def calc_area(self,a,b):`` Calculates the area of the rectangle from the points a and b, first it finds the horizontal distance by taking the b value and subtract it from the a value. The same is done for the vertical height. These two values are then multiplied to form the area of the rectangle.

In the function ``def find_biggest_area(self):`` We take all the coordinates and calculating the area for the rectangles for each of these coordinates, this value is then stored in the ``self.max_area`` and is compared against future areas to find the overall largest. This then updates the object variable.

The ``main() -> none:`` function runs the previous functions to return the program output. The ``-> none:`` is an optional type hint that shows that the function does not return anything. Inside the function the "day09" class is created and initialised, in turn creating the "max_area" and "coords" variables. It then loads in the data with ``day.open_and_store()`` and finally runs ``find_biggest_area`` to return the largest area from the coordinates. The largest area is then returned.

The last two lines are important for when importing the file, although it does not matter much in my case, they ensure that when the file is imported into another file none of the file is run. 

### Maximising efficiency: ###

As the code was based on an another developers existing solution some of the parts included are not relevant to my use case or could be improved in other ways, the first improvement I made was in ``def find_biggest_area(self):`` where, instead of starting the second loop from the first value I started it from the "i" value, this reduces duplicates and self comparisons to make a more accurate program. 
``` python
        #for i in range(len(self.coords)):
            #for j in range(1,len(self.coords)):
        for i in range(len(self.coords)):
            for j in range(i + 1, len(self.coords)):
```
Another improvement I made was to remove the last line that means when the code is imported it doesn't run- I removed this as I will not be importing it anywhere, this required a bit of tweaking as it wouldn't work without first ensuring the function returned something.

## Task 2: ##

For part two the challenge is made slightly more difficult by only allowing red or green tiles to be switched out. Red tiles are connected to each other by a line of green tiles, wrapping over lines. Within these sections all the tiles are either red or green. Now, any rectangle has to have red tiles in the corners- ***and*** be filled with only green or red tiles.

 ### Explaining the code top to bottom:###