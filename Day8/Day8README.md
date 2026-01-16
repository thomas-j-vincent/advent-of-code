# Day 7

## Task 1: ##

On day 8 we need to use euclidean distance to help some elves connect electrical junction boxes so they can form an light installation. Having connected the closest 1000 pairs of junction boxes we need to multiply the size of the three largest circuits to get our puzzle answer.

 ### Explaining the code top to bottom:###

We first import the math module so we can calculate the euclidean distance between the junction boxes. 
Having opened the file we split it into lines and then split the lines on commas to get the three coordinate components, we then convert those values into integers so they can be properly treated as numbers before putting them in a list. This results in a list where each entry is one set of coordinates.
edges is every possible two-box combination of connections, it ensures the first value is smaller than the second value by iterating through incrementally from the start instead of randomly- removing the chance for duplicates.