# Day 7

## Task 1:

On Day 7 we find ourself in the teleportation room! However, the teleporter seems to be broken and we need to fix it. According to the manual there is an issue with one of the **tachyon manifolds** they work as follows: 
A beam starts from the position **S**, always moving downwards. They pass freely through empty space (.) however if there is a splitter (^) the beam at that position stops and "splits" to the immediate right and immediate left of it. We need to calculate the amount of times our beam gets split.

My initial approach was to render the program as you would if you were doing it by hand however, this was very resource intensive and had no way of stopping the beam continuing from the splitter- it would render next to it but then continue on its path in the next row. To solve this I started following a youtube video by HyperNeutrino. 

 ## Explaining the code top to bottom:##

The first line 
```python
from collections import deque
``` 
imports the deque function from the collections module, this allows characters to be quickly appended to the right and left of a list- this will be paticularly useful for moving the beam when split.
We then open the input file as f and then use ``grid = [line.strip() for line in f]`` to get a grid of characters whereby each line in the input is a entry in the list. 
To find where the **S** character is we enumerate through the rows and characters within the rows, only keeping "S" values. The variables r and c return the coordinate position of the character.
To ensure we do not loop over the same splitter multiple times or end up tracking a single route through the splitters we store beams and seen. We use deque for beams so that we can store the coordinates of the beams, and use popleft() to move through them quickly. Seen does not require deque as although we store all the coordinates of positions we have iterated over we do not need to cycle through them. 

The function ``` def add(r,c): checks to see if the current beam location has already been iterated through- meaning the splits have been counted- and if it has (and is therefore in the seen list) it returns the function. Otherwise it adds it into the list.

Here we also declare the count variable, counting the number of times the beam has already been split (our puzzle output).