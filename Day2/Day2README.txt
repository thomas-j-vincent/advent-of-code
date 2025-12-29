Day 2

Task 1:

For day 2 we have to determine which product ID codes are erroneous by following a set of rules, they are as follows:
Any ID codes where the first character is 0 and any code where the number is composed of a twice repeating set of patterns is fake such as 11, or 1010
most importantly the ID codes are ranges so the program has to loop through each number in a range to find the numbers.

 Explaining the code top to bottom:

I first open the Day2 Input file and write each line to the string "text", removing any whitespace with the .strip function.
Then I write the "text" string to the "numbers" list, splitting the values by the commas in between them. This creates a iterable list where each entry is
a range to be iterated through.
The running total is then defined as 0 so it can be counted without being reset accidentally.

The function check_odd_even requires both the number to be checked and the number we are dividing it by, returning the result as a string "Even" or "Odd"
The if loop uses the % operator to find the remainder of the division between the number and the divisor, therefore being able to tell whether the result
is even or not. Therefore, if the result is 0, the function returns "Even" and if not it returns "Odd"
(This function was removed to make the program run more efficiently)

The for i in numbers loop is used to iterate through the values in the range
I then chose to split the list value at dash point, then converting it to an integer. This allows us to iterate from the start of the range to the end. 
Here we enter another if statement looping through each number in the range
for each number I first chose to remove any numbers that were not even in length
 (as there is no way a set of characters can repeat twice if the length is uneven)
if the number is two characters long, i then check if the number can be divided by 11
 (as all twice repeating numbers in 2-character long number are divisable by 11)

from here we take the number of digits and half them, so as to discover how long the the start and end pattern should be. we then convert it to an integer
to find the minimum number that would pass the test, we take the length of the start section, put a one at the front, and fill the rest with zeros then 
stitch the front and back section together.
we then do the same but replace all the numbers with 9's, to get the largest possible number that would pass the test.

we then compare the values from the range with these predetermined minimums and maximums, and if it is between them we split the number two
if the left and right are equal we return TRUE, otherwise we return FALSE.
from there we have an if loop, that adds to the total if allMatch is TRUE

then we print the value.

Maximising efficiency:

Initially my aim was to skip as many numbers as possible, quickly removing them from the loop allowing the program to process as few numbers as possible however,
this led to redundant processes
In the code you will see lines that are commented out, these are lines that were in the code however, I took them out to increase the speed the program takes to run.
I did this by attempting to decrease the amount of loops or functions called, as loops slow down the program whilst it iterates through them.

The first way I did this was to remove the check_odd_even function, instead choosing to use the modulus operator outside it. 
I then removed the entire loop when checking if the number is divisable by 11, as we do that functionality later anyway.
I also removed the segment that checks is the values are above the minimum and below the maximum, as that we can just check each number individually
Finally I skipped reassembling the halves as that value was the same as the "value" string from earlier which we use in the allMatch loop to add to the total. 
