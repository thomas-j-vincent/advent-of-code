Day 3:

Task 1:

We had to find the largest two-digit number that could be made from a set of 15 characters. The first digit of this number has to be to the left of the
second digit, we then had to sum these values with all the others found in the input values.

My idea was to first loop through all the numbers (excluding the last one) in each line, checking to find the largest possible number. I would then loop
through the remaining numbers to find the second digit.

 Explaining the code top to bottom:

I first open the Day3 Input file and write each line to the string "text", removing any whitespace with the .strip function.
I then replace any linebreaks with commas by using the .replace function. This then overwrites the old text value.
Then I write the "text" string to the "numbers" list, splitting the values by the commas in between them. This creates a iterable list where each entry is
a range to be iterated through.
The running total is then defined as 0 so it can be counted without being reset accidentally.
We then enter a for loop, iterating through all the values of i, here I declare all variables that need to be reset for each value such as: 
maxValue (the largest digit, starts as -1 so everything is bigger), previousMaxValue (used to store the maxValue before maxValue was overwritten),
maxIndex (stores index of the maxValue) and minValue(stores second character).
Then for the length of the input, "digit" is the value of the digit in the number. If "digit" is greater than "maxValue", "previousMaxValue" becomes 
"maxValue", "maxValue" becomes "digit" and "maxIndex" becomes "index". If "maxIndex" + 1 == "length" then the "minValue" becomes the "maxValue" and
"maxValue" becomes the "previousMaxValue" as there are no characters left for the second digit in this case.
The second for loop finds the second digit when the maximum value isnt the last one and works by setting the range as a for loop where "index" must be
bigger than "maxIndex" and sets "minValue" as "digit" as long as "digit" is larger than the current "minValue".
The last two lines add the two digits ("maxValue" and "minValue") as a string so they get placed next to each other rather than actually added, converts it
to a integer and then adds it to the total.
The program then prints the total.

Maximising efficiency: 

Here I tried to remove as many variables that had to be constantly calculated and instead replace them with set integers. The first case of this happening 
is "length" which I replaced with 100, as all input lengths were 100.
Another way I tried to maximise efficiency was by removing excess loops and using built in python calculations, in this case I replaced finding the digit
by doing "digit = number[index]" and instead used "enumerate" to pass the index and the digit for that index. This meant I was able to remove "number"
entirely.
The last way I made my program more efficient was by trying to reduce the line usage without impacting readability. I only did this in one case by replacing
 "temporaryTotal = str(maxValue) + str(minValue) temporaryTotal = int(temporaryTotal)" with just "temporaryTotal = int(str(maxValue) + str(minValue))"

Task 2:

In task two instead of the largest combination of two digits we need to find the largest combination of 12 digits:
My first idea was to repeat the loop used for finding the first two values another ten times, making up the other digits however, this would've been very
slow so I chose another method. Instead I chose to put all of the characters from a line into a list, determine the amount I have to remove, and then
whilst the previous number is larger than the current number it removes the current number to end up with the largest possible twelve digit number.

 Explaining the code top to bottom:

The first 9 lines are the same from the previous program however once in the for loop we define "digits" as a each character in each line.
I then define "removes" as the length of the line - 12 (the twelve characters we have to keep) we then declare our list "result" which is where the results
get appended. I then loop through the digits in "digits" and while there is at least one digit in "result", there are "removes" remaining and the last digit
is smaller than the current digit I remove the current digit from the "result" list, and then I reduce the amount of "removes" left. This continues until
there are no "removes" left. The remaining digits are then appended to "results". If for some reason there is still more than twelve digits in the result
list, we then shorten the digits from the right. The last four lines take the temporary result, convert them into one number using ".join" and then adds it 
to a running total. 
The final total is then printed

Maximising efficiency:

In this code there wasn't many obvious ways to imporve the efficiency apart from converting "removes" from a calculation ("len(digits) - 12") to a set value
as the length is always this same. I had initially wanted to remove the variable completley but it gradually gets subtracted through the loop, meaning a
defined value would cause an error.