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

### Maximising efficiency: ###