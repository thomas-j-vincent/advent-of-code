# Day 10

## Task 1: ##

In day 10 we have a set of machines and a row of buttons, for each machine (line in the input) we have multiple buttons and need to select the smallest number of buttons to turn on all the lights of the machine. However, some buttons control more than one light - and the lights aren't all necessarily off in the first place.

This solution uses sets of indices to simulate the lights, as the program optimises for least button presses this automatically finds the most efficient option.

 ### Explaining the code top to bottom:###

We start by creating a "total" variable, outside any loops so that it could track the number of steps required to achieve the all lights on. 

We start by creating a loop that reads line by line- and then removing the whitespace at the start and the end of the input. It then checks for square brackets using the `\` to escape the character. It then captures any "." and "#" keys preceeding it (the line makes sure to keep capturing multiple characters with the "+"), the second capture group used `\d` to capture any digits and `,` to capture commas. (this captures lines such as "(1,2) (3,4,5) (0)"). The third capture group uses `\{([\d,]+)\}` where the "\d," captures digits and commas, and the plus ensures all the characters are captured. 
These captures are then stored as variables: target, buttons, and then _ (to disregard the value).
The next line converts the stored characters into values, where the "#" keys are stored as numbers, telling the program that these indexes need to be turned on - therefore making comparisons very easy.
The next line also converts "buttons" into sets; first it splits on spaces, converting a single string into two values of a list; then we remove the square brackets associated with a list with ` button[1:-1]`; these values then get split on the commas - so we get two lists, containing the individual characters. `map(int, ...)` converts the strings into integers and then `set(...)` transforms these lists into a set of the light indices - so they can be compared later.
`for count in range(1, len(buttons) + 1):` loops through the number of buttons up to the whole number, the next line uses itertools to generate a combination of buttons to "press" that would turn on the lights. For example for a count value of 2 this would be the the buttons that are pressed:
 ```python
(buttons[0], buttons[1])
(buttons[0], buttons[2])
(buttons[1], buttons[2])
```
`lights = set()` is the line that actually simulates the buttons being pressed
The "^=" operator in the next loop is called a symmetric difference and makes the value act as a toggle, therefore modelling the button presses where lights is the value of which light is on and buttons is the index of the buttons that need to be switched.
`if lights == target:` compares the current light value to the intended value - and if all the lights are on it sets the total as the number of button presses that were required and then breaks out of both loops. This allows the program to move onto the next line. 

Once all lines have been calculated the total is printed.

### Maximising efficiency: ###

As the code starts from the fewest number of button presses it is already as efficient as it can be. Although there are lots of loops I cannot currently think of a way to remove these loops unless there was some way to store all the different combinations of button presses - but even if there were there would be no way to "guess" their impact on the lights so this would have to be individually calculated anyway.

## Task 2: ##

In task two, instead of attempting to turn on the lights we use the buttons to set numeric counters to a specific joltage value that shows the correct joltage is being recieved. All these counters are initially set to zero and the last set of numbers dictates what values each counter needs to end up at.

This code first generates all the different button press combinations, and then detects which buttons were pressed an odd number of times - this allows it to only focus on buttons that make a difference to the actual light output.

 ### Explaining the code top to bottom:###

First we import the required functions: collections (used to create dictionaries and detect the parity of the buttons, whether they are odd or even), functools (caches function calls) and itertools (generates all possible combiantions of button presses)

The function `def powerset(s):` generates every possible subset of s, at size r - s comes from the buttons variable (from the file).

The function `def solve(line):` determines how which buttons and how often they need to be pressed to get the required output. It first takes the line from the file and sets the inputs as variables: lights, *buttons (the * means that everything in the middle is part of the buttons variable), demands using `line.split()` to split the lines at the spaces and `g[1:-1]` to remove the brackets off the start and end of all of the variables. at the end of this line the variables will have values such as this:
```python
lights  = "#.#."
buttons = ["0,2", "1,3"]
demands = "2,1,0,3"
```
Lights then gets converted to a tuple so that every "#" mark is a true, and every "." is a false
Buttons becomes a set containing the affected buttons by index so instead of `["0,2", "1,3"] it is {0,2} {1,3}
Demands then turns into a list of integers so the numbers can be properly accessed in the correct format.
This line `options, output = collections.defaultdict(list), dict()` is part of the program designed to precompute all the button combinations - in paticular it groups the buttons by their true or fals value (stored as options) and output which stores the exact supply values. 
The for loop loops over for the amount of buttons there are in the paticular line. For each of these lines "supply" is which buttons are affected by the button, this then gets turned into parity (removes any even numbers so the values are either 0- for unaffected- or 1 - for toggled)
The next line ensures that the parity can be stored so that it can be referred back to without having to be recalculated. 
The next function `def opt(demands):` is nested in the `@functools.cache` wrapper, this means that if `opt((2,4,6))` is called again then the answer doesn't need to be recalculated and is instead "remembered" by the computer. However, the recursion (when the answer is stored) stops when any of the answers return negative - meaning that the program effectivley stops if any issues arise

### Maximising efficiency: ###

There are some ways this code could be optimised such as using `ast.literal_eval()` instead of eval() as it is slow. 
We could also use: 
``` python
button_vectors = [
    [1 if j in btn else 0 for j in range(len(demands))]
    for btn in buttons
]
```
instead of checking j in buttons[b] each time.