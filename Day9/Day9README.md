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

The plan of attack for this code was to first build a compact matrix representing the entire space using coordinate compression, then slice out all possible rectangular regions and check whether they contain the valid characters.

 ### Explaining the code top to bottom:###

The first lines we use are to import the required modules for this code to work, we use pandas to read the file and numpy to do number formatting.

It then reads the input and stores it as a pandas dataframe, where D9[0] is all the x values and D9[1] are all the y values.

In these lines we then compress the coordinates, this is done by using numpy to exchange the (often large) coordinate values into different, smaller, integers that keep their relative sizes. This reduces the size of the coordinate grid used but still allows the area to be calculated.
```python
unique = np.unique(D9[[0, 1]])
factors = np.arange(len(unique))

D9[[0, 1]] = D9[[0, 1]].replace(unique, factors)
```
As standard lists are quicker to access and ammend than pandas dataframes we then store all the x and y values in seperate lists as we do not need the specialist functionality of the dataframe anymore.

We use these values to create a single grid containing all the values and using `np.zeros` we can fill the grid with zeros, except if it is filled - in that case it is a one value. We mark each coordinate in the input as filled in the grid - using:
``` python
for i in range(len(D9)):
    s[y[i]][x[i]] = 1
```

Having got a grid of all list values (from the input) we then have to mark the edges between them to *draw* the rectangles. This is done in many loops, it goes through each line and; if two values are aligned on the x axis it *draws* a line between them, same on the y axis. 
```python
for i in range(len(D9)):
    for j in range(len(D9)):
        if i != j:
            if x[i] == x[j]:
                for k in range(y[i], y[j]+1):
                    s[k][x[i]] = 1
            if y[i] == y[j]:
                for k in range(x[i], x[j]+1):
                    s[y[i]][k] = 1
```
We then use scanline fill to find all the borders, and if there are atleast two we assume the space between them is a shape. filling them and turning the outline into a filled rectangle.
``` python 
for i in range(len(s)):
    border = []
    for j in range(s.shape[1]):
        if s[i][j] != 0:
            border.append(j)
    if len(border) >= 2:
        for j in range(min(border), max(border) + 1):
            if s[i][j] == 0:
                s[i][j] = 1
```
To generate all possible rectangles we loop through all values in D9 and uses the biggest values and assigns them to x2 and y2, and the minimum values for x1 and y1. If any either x1 and x2 or y1 and y2 are equal we skip this value - as this is not a rectangle.

we then use this line to calculate the actual area of the rectangle, using `unique[x2]` to uncompress the previously compressed coordinates.

These are then sorted, into largest first, and then getting incrementally smaller.

To check that these rectangles are full we loop through, checking for 0 - if present there is a gap and the rectangle is invalid.
``` python 
for i in range(len(m)):
    r = [row[m[i][0]:m[i][2]+1] for row in s[m[i][1]:m[i][3]+1]]
    if any(0 in j for j in r):
        continue
    else:
        p2 = m[i][4]
        break
```
We then print the largest value.

### Maximising efficiency: ###

The code solution adapted for this task had originally also been used to solve task 1, this meant that some of the school of thought wasn't adapted for efficiency - such as removing invalid rectangles sooner to avoid processing them for as long. 