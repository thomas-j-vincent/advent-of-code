We had to record the amount of times a dial went past 0 based on the inputs where a L in front of the number meant subtracting the number and an R in front of the number meant adding the number. 

There are two programs for Day1 task one, the first is called AdventOfCodeCharacterConverter and exists to take the numbers out of there vertical format and into a python acceptable list. (this is then repeated in the actual file but I hadn't figured out how to do that at that point)

 Explaining the code top to bottom first I imported the numbers as a text file and removed any white spaces or linebreaks from the ends to make the file more uniform.
 I then used the .strip function to replace any white spaces within the file with commas, to make the file a list that could be iterated through.
 I then stored the number that the program was currently at and defined it as 50 as that is where the brief said we were to start. 
 zeroOccurences was also stored outside any for loops so it didn't accidentally reset during the code.

 The function isZero checks if the current number is zero and if it is it adds one to the Zero occurences variable we just defined, making sure to return the new value otherwise none of the other functions will be able to access it. It then prints the amount of zero occurrences by assigning it to a string so the variable could be read (this is inefficient as by adding an f before the print message the same outcome is possible) instead of:  txtB = f" isZero, occurences: {zeroOccurences}" and then: print(txtB)  we could just do: print(f" isZero, occurences: {zeroOccurences}") as it only takes up one line

The function isMaxOrMin creates the loop  effect by subtracting 100 if the currentNumber is above 99 and adding 100 if the currentNumber is below 0. It then returns currentNumber and zero occurences so it can be updated globally. (zeroOccurences is not required, this was left in when I was incorrectly testing zeroOccurences too often out of fear of missing one, this created false counts)