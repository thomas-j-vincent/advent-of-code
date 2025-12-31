Day 5:

Task 1:

On day 5 we have to find the spoilt fruit, we get given the ranges that include fresh fruit and then the number of the fruit we have to compare.

My idea was to create a list of valid ranges, then iterate through it with the numbers we need to test if they are valid again.

 Explaining the code top to bottom:

In the first two lines we open the file "Day5Range.txt", this is a file comprimised soley of the range portion of the input, created manually. we then map
this to "between", removing any whitespace in the process.

We then open the file "Day5Input.txt", a file comprimised of soley the fruits we need to test, we define this as numbers, removing whitespace in the process
but also converting it to an integer. 