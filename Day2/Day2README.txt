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
 (as all twice repeating numbers in 2-character long number are divisible by 11)

from here we take the number of digits and half them, so as to discover how long the start and end pattern should be. we then convert it to an integer
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
I then removed the entire loop when checking if the number is divisible by 11, as we do that functionality later anyway.
I also removed the segment that checks is the values are above the minimum and below the maximum, as that we can just check each number individually
Finally I skipped reassembling the halves as that value was the same as the "value" string from earlier which we use in the allMatch loop to add to the total.

Task 2: 

In task 2 it was discovered that invalid IDs could also be singular digit repeating numbers such as 111

 Explaining the code from top to bottom: 

In the second task I attempted to remove the for i in numbers for loop by creating another list containing the start and end values from the ranges instead.
This reduces the amount of loops the code has to go to and therefore speeds up the program, I attempted to do this with the previous task however,
I structured the entire code around this loop, with no way to determine between start and end values from different ranges and therefore kept it the same.

For the function generate_invalid_IDs I used the function from someone's solution found on reddit (I can't find their name) but this is the way it works and
how I optimised it for purpose of only solving the second task:
The first line finds the total length of the highest number possible by taking the max_value (passed to the function), finding its length and then
converting it to an integer. All the invalid numbers in the range are stored as a set so it can be passed back to the program to iterate through. This works better than my system as it means the program doesn't have to find all the invalid IDs each time, only once for each range (speeding up the program).They then enter a for loop to iterate through the length of the number, starting at the second value, as the first digit is used to compare against the others-it has to be valid. For each number length d is used to calculate possible repeating sections ie. for an eight digit number d would be 1, 2, 4. If a the length of the number has a remainder when divided by d, that d value is skipped as there can be no repeating sections for a number of that length i.e. d=3 and L= 8, 8 cannot have repeating sections of 3. t is the amount of times the section has to repeat to fill the number of that length
i.e. if d=4 L=8 t=2. The if loop "if part 2 and t < 2:" was intended to ensure that the repeating section always repeats at least once, and can therefore be removed to increase the program speed. Start and End are then created as the highest and lowest possible numbers. From this range it loops through from the lowest number to the highest, taking the current value and multiplying it by the times it has to be repeated for that d value. If the number created from that function is greater than the maximum value it stops the loop, otherwise it adds the number to the invalid ID set.
This set is then returned.

For the function solve_ranges I also used a solution found on reddit, this is how it works:
The first line finds the maximum value in each range, we then call the generate_invalid_IDs function to return the list of invalid IDs, total is then
declared as zero, which will be added to find the ultimate answer. The for loop loops through the invalid IDs and for each number in the range as long is
between the maximum and minimum for that function, gets added to the total. The loop is then broken out of to ensure there is no double counting.
Total is then returned.

The answer is then printed.

Maximising efficiency:

The code given was initially to solve both the first and second task, as that was not required I first removed where the part2 argument was passed, and
defaulted it to true. I also removed the "if part2 and t < 2:" loop as part true is always true as is t < 2. 