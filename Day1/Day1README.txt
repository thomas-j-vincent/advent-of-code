Day 1

Task 1:

We had to record the amount of times a dial was pointing at 0 based on the inputs where a L in front of the number meant rotating the dial to the left and
vice versa. The number next to the inputs determines how much we rotate the dial in said direction.

There are two programs for Day1 task one, the first is called AdventOfCodeCharacterConverter and exists to take the numbers out 
of their vertical format and into a python acceptable list. (this file is no longer required)

 Explaining the code top to bottom:

first I create an empty list called values, this allows us to store all the inputs of the file and iterate through them, ensuring we do not miss any.
I then open the Day1Input file and go through it line by line, using the strip function to put them all on one line and then append them to the values list.
I then move the values to the string "formatted", by doing this I can then remove any whitespace in the values (and replace the quotation marks but this 
isn't necessary)
The values from the "formatted" string is then moved into the numbers list, ensuring the values can be iterated over.
I then stored the number that the program was currently at and defined it as 50 as that is where the brief said we were to start. 
zeroOccurences is the value we are aiming to find and was also stored outside any for loops so it didn't accidentally reset during the code.

The function isZero checks if the current number is zero and if it is it adds one to the Zero occurrences variable we just defined, making sure to return the
new value otherwise none of the other functions will be able to access it. It then prints the amount of zeroOccurrences by assigning it to a string so the 
variable could be read (this is inefficient as by adding an f before the print message the same outcome is possible)
instead of:  txtB = f" isZero, occurences: {zeroOccurences}" and then: print(txtB)  
we could just do: print(f" isZero, occurences: {zeroOccurences}") as it only takes up one line

The function isMaxOrMin creates the loop effect by subtracting 100 if the currentNumber is above 99 and adding 100 
if the currentNumber is below 0. It then returns currentNumber and zero occurrences so it can be updated globally. 
(zeroOccurences is not required, this was left in when I was incorrectly testing zeroOccurences too often out of fear of missing one,
 this created false counts)

The for i in numbers loop iterates through the numbers array and does two things:
 if the first character is an L it removes that character, converts the remaining number to an integer and then subtracts it from the current value
 if the first character is an R it removes that character, converts the remaining number to an integer and then adds it to the current value
it then checks whether the currentValue is outside the terms of the loop and needs to be brought back in range, and then checks if the number is pointing at
zero or not, by calling the function isZero

Task 2:

In task 2 we had to count anytime the counter pointed to zero, even if it didn't end up there
We use the same input values as task 1 so therefore there is only one file for task 2.

 Explaining the code top to bottom:

The first 19 lines of task 1 and task 2 are the same, the first differences being from the function isZero
I started by adding a movement parameter that is passed to the isZero function, this passes the value of the numbers from the input to tell the function how
much it has to move. 
I also had to add in a step value, either 1 if the movement is greater than 0 or -1 if not. As we have to check if the counter ever point to zero I added in
for loop, checking if the value of currentValue is within the constraints of the loop or not. the function also checks whether the value is equal to zero or
not, adding to the zero counter if it is.

Outside the function, I have a for loop that iterates through the numbers one by one. Taking the direction and using it to determine whether movement is the
positive of value or its negative (negative if L, positive if R) 
The function isMaxOrMin is then called to determine how many times the function passes through 0.

Finally the answer is printed.