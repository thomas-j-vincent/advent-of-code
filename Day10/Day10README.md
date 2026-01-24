# Day 10

## Task 1: ##

In day 10 we have a set of machines and a row of buttons, for each machine (line in the input) we have multiple buttons and need to select the smallest number of buttons to turn on all the lights of the machine. However, some buttons control more than one light - and the lights aren't all necessarily off in the first place.

This solution uses sets of indices to simulate the lights, as the program optimises for least button presses this automatically finds the most efficient option.

 ### Explaining the code top to bottom:###

We start by creating a "total" variable, outside any loops so that it could track the number of steps required to achieve the all lights on. 

We start by creating a loop that reads line by line- and then removing the whitespace at the start and the end of the input. It then checks for square brackets using the `\` to escape the character. It then captures any "." and "#" keys preceeding it (the line makes sure to keep capturing multiple characters with the "+"), the second capture group used `\d` to capture any digits and `,` to capture commas. (this captures lines such as "(1,2) (3,4,5) (0)"). The third capture group uses `\{([\d,]+)\}` where the "\d," captures digits and commas, and the plus ensures all the characters are captured. 
These captures are then stored as variables: target, buttons, and then _ (to disregard the value).
 

### Maximising efficiency: ###

## Task 2: ##

 ### Explaining the code top to bottom:###

### Maximising efficiency: ###