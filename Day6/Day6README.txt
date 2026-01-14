Day 6

Task 1:

For this day we had to take the values in the input, and either add them, or multiply them however, you take the values by column instead of by row. 

Initially I tried to seperate the data into lines, and then i could take the first value of each -iterating through the rows- appending these to a running total list, then depending on the operator I either multiply the values or add them. However this resulted in an incorrect value (by 12) 

 Explaining the code top to bottom:

The first line imports the prod Method from the math library, this allows a program to return the product of any iterable. 
Then we define the "total" as 0, out of any loops so that it doesn't reset as well as the lists "lines" and "ops" 
The fourth line defines the "operands" dictionary, this stores the operators + and * as keys to a dictionary where the value is a small function (lambada) that applies the operator to it's given list of numbres.
We then open the file, writing each line to a new entry in the list "lines".
We then take the values from the fourth line and appends it to the list "ops".
Then we take the first four lines, put them in the list "lines" and convert it into integers so the values can be handled as numbers.
The next line takes all the lines and takes them out of their lines and groups them by position in the lines not by line (stops you from having to iterate through each value of each line)
Then, for the length of the line, it uses the operator on the numbers on that line.
The answer is then printed.

Maximising efficiency:

I didn't have to improve the efficiency of this program however, there were some improvements that made it better than my previous iterations. One of these includes using the lambada functions to compute the values of the lists rather than having to enter if statements. Another improvement was the zip function that removed the need to iterate through all the values of the lines.

Task 2: 

Task 2 required the numbers themselves to be read in columns, right to left. So that a column of values 64, 23, 314, +  would look like this laid out flat 4 + 431 + 623.

 Explaining the code top to bottom:

The first line tells systems to use python 3 to run this file, useful for when the file is run on linux or mac systems
Import sys allows the user to use the command line to pass arguments such as the file we want to open when we run it instead of hardcoding it into the file. It also allows
conversion limits which are set to allow different recursions (functions calling themself) than default python.
From typing import list allows strings to be converted into lists.
sys.setrecursionlimit(100000) uses the sys function declared earlier to increase the maximum times a loop can repeat.
The next line allows the filename to be inputted from the commandline however, I hardcoded it in the line below as I knew what the name of the file was going to be anyway.

The function "linesToList" returns a list of strings, First it creates an empty list where every element is a string as a place to store lines from the file.
We then open the file declared above (using with to ensure the file is automatically closed afterwards). It then loops through every line in the file, removing newline
characters and appends the line to a string called lines. 
Lines is then returned from the function.

The function "partTwo" first calles the function "linesToList" gives the value to "lines". A final variable "answer" is then declared as 0, allowing it to be
increased as the file progresses. "problems" is a list of the numbers that need to be added or multiplied for each solution, "operations" is another list
which stores the operators for the paticular problem. "operations" is given the value of the last line of the file and is stored in a list. "digitLines" then
takes all the lines (except the last line) as vertically aligned digits. The length of each of these lines is stored in "lineLength". "problem" is an empty
list created to hold the numbers of a singular problem. The for loop loops through all the numbers in the line length, first declaring a value integer, as well
as a boolean flag to detect empty columns. There is then another for loop that loops through each row at the current column and if it is a digit creates a number
from the vertically aligned characters. The flag allSpaces is set to Flase -signalling that the column contains data- if it were empty we end the problem
and start a new one, otherwise we add the number to the current problem, and then add that to the larger problems loop. We then loop over each problem and its
corresponding operator, setting the result as zero and if the operator is "*" we multiply them, setting the result to 1 first (as 0 * x = 0) otherwise we
add them. The result is then added to the answer. 
The answer is then printed

The program then calls the function.