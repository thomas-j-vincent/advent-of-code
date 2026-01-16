# Day 7

## Task 1: ##

On Day 7 we find ourself in the teleportation room! However, the teleporter seems to be broken and we need to fix it. According to the manual there is an issue with one of the **tachyon manifolds** they work as follows: 
A beam starts from the position **S**, always moving downwards. They pass freely through empty space (.) however if there is a splitter (^) the beam at that position stops and "splits" to the immediate right and immediate left of it. We need to calculate the amount of times our beam gets split.

My initial approach was to render the program as you would if you were doing it by hand however, this was very resource intensive and had no way of stopping the beam continuing from the splitter- it would render next to it but then continue on its path in the next row. To solve this I started following a youtube video by HyperNeutrino. 

 ### Explaining the code top to bottom:###

The first line 
```python
from collections import deque
``` 
imports the deque function from the collections module, this allows characters to be quickly appended to the right and left of a list- this will be paticularly useful for moving the beam when split.
We then open the input file as f and then use ``grid = [line.strip() for line in f]`` to get a grid of characters whereby each line in the input is a entry in the list. 
To find where the **S** character is we enumerate through the rows and characters within the rows, only keeping "S" values. The variables r and c return the coordinate position of the character.
To ensure we do not loop over the same splitter multiple times or end up tracking a single route through the splitters we store beams and seen. We use deque for beams so that we can store the coordinates of the beams, and use popleft() to move through them quickly. Seen does not require deque as although we store all the coordinates of positions we have iterated over we do not need to cycle through them. 

The function ``def add(r,c):`` checks to see if the current beam location has already been iterated through- meaning the splits have been counted- and if it has (and is therefore in the seen list) it returns the function. Otherwise it adds it into the list.

Here we also declare the count variable, counting the number of times the beam has already been split (our puzzle output).
The while loop marks the start of the tracking process. While beams are greater than 0 (meaning S has a coordinate):
- the current coordinate removes the first beams value, and assigns it to r, c
- If that position is a "." (air) or an "S" (the start):
- - If it is on the edge of the grid skip it
- - otherwise, we add the next position beams would be in (vertically below the current one)
- If the position is a "^" (splitter):
- - add one to the count (the beam has been split)
- - add the list position to the left and the list position to the right to the beams list.

We then print the value of count.

### Maximising efficiency: ###

The way to maximise efficiency with this problem was not to try to physically draw out the grid as if you were a human, but instead to only record the parts that matter to the problem; the amount of times the beam has been split; and where the beams are.

## Task 2: ##

In task two it turns out that the **tachyon manifold** is actually a **quantum tachyon manifold**, this means that only a single beam is sent through the manifold -taking both the left and right sides of the splitter- as this is impossible time splits whereby in one timeline the particle goes left, and in the other it goes right. We need to find the total number of active timelines after all paths have been run, essentially counting every possible route the particle can take.

 ### Explaining the code top to bottom:###

The first line imports the cache function, which enables the store function to be "saved" so that each path doesn't need to be entirely recalculated each time.
The program then opens the file and stores the "beams" and "seen" variables the same way as before.

The function ``def solve(r,c):`` takes the coordinates the "S" character and calculates all the number of timelines reachable. 
If the row value is greater than the length of the grid the only amount of timelines possible is 1 (as there is no space for any splitters).
If the coordinate is a "." or a "S" we just pass the beam through by adding one to the row coordinate (returning the same location but one position lower) and return that value.
If we reach a splitter we want to pass the indexes to the left and right of the splitter back to the function so it can run it from those position. 
The function then returns the amount of different timelines by letting the function run through them all, and if they reach the bottom it adds one to the return value.

The program then repeats this value.

### Maximising efficiency: ###

In this program to maximise efficiency we used the cache tool, this prevented adding to any global variables or running any functions more than needed.