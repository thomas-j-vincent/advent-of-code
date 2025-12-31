Day 5:

Task 1:

On day 5 we have to find the spoilt fruit, we get given the ranges that include fresh fruit and then the number of the fruit we have to compare.

My idea was to create a list of valid ranges, then iterate through it with the numbers we need to test if they are valid again.

 Explaining the code top to bottom:

In the first two lines we open the file "Day5Range.txt", this is a file comprimised soley of the range portion of the input, created manually. we then map
this to "between", removing any whitespace in the process.
We then open the file "Day5Input.txt", a file comprimised of soley the fruits we need to test, we define this as numbers, removing whitespace in the process
but also converting it to an integer. 
We create a set called "fresh" to house the results, we use a set because it doesn't allow duplicates. Ensuring there are no repititions.
I then start a loop, looping through the numbers in between, defining a start value and an end value by splitting the between inputs at the hypen.
The "for number in number:" loop goes through all the numbers and if the number is between the start and end value it gets added to the "fresh" set.
At the end the length of the set is calculated using the .set() function.
This result is then printed.

Maximising efficiency:

There is no simple way to make this program more efficient.

Task 2: 

In task 2 we ignore the available ingredients and instead sum the number of fresh IDs

Initially I intended to use the same method as the prior program however, just skip the comparison to the ingredients.
As this method was very inefficient I instead decided to take the lowest and highest values of each line, subtract duplicates, and then use the start and
end values to sum the total fresh IDs.

 Explaining the code top to bottom:

As we only need the ranges in this program that is the only file we open. We define ranges as an empty list and for every line we split the ranges at the
hypen, defining the values as variable start and end, we then append these values to ranges. Providing us with a list where every entry is two values, the
start and the end for that line. We then sort the ranges list to get the highest and lowest values in order, helping us understand which values are repeated
Using the merged list, we remove any duplicates. This is done by first creating a start and end value from the tuple (from first value of ranges list)
we then use the for loop to change check whether a value fits within these ranges, if it does it gets discarded