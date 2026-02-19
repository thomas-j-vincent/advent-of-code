# Day 11

## Task 1: ##

In Day11 we are tasked to count all of the possible connections from "you" to "out", the input is organised as follows: The three letters on the left are the input, and the sets of three letters on the right are outputs, we need to iterate through these outputs linearly (no going backwards) until we reach "out". We should then return how many possible paths there are.

 ### Explaining the code top to bottom:###

We first import the cache function, this helps us store some of the results so we do not have to compute them each time they are called, such as when partially going over a route we have already covered.
We then create graph, which is currently an empty dictionary that we then add the inputs, and their outputs into.
We then open the file and for each line split at the colon into inputs and outputs, the inputs ate then put into the first part of the dict and the outputs are split again into the seperate entries into the other.
The cached function "count", takes the input and output from the graph dict and if they are same value returns 1. Otherwise the function sums the output with the input (if there is one) for every input.
The final line calculates and prints the total number of paths through the input from "you" to "out"

 ### Maximising efficiency: ###

This file is already pretty efficient as it stores most of the work in the computer cache so it doesn't have to redo it.

## Task 2: ##

Task 2 is similar to task 1 however this time we know that the path has to go from the server rack (svr), though the digital to analog converter (dac) and the fast fourier transformer (fft) in any order, this helps us limit the loops the code is taking.

 ### Explaining the code top to bottom:###

We first import the cache function, this helps us store some of the results so we do not have to compute them each time they are called, such as when partially going over a route we have already covered.
We then create graph, which is currently an empty dictionary that we then add the inputs, and their outputs into.
We then open the file and for each line split at the colon into inputs and outputs, the inputs ate then put into the first part of the dict and the outputs are split again into the seperate entries into the other.
The cached function "count", takes the input and output from the graph dict and if they are same value returns 1. Otherwise the function sums the output with the input (if there is one) for every input.
The final line calculates and prints the total number of paths through the input, but only the ones includint the dac, fft, svr and out.

 ### Maximising efficiency: ###

This file is already pretty efficient as it stores most of the work in the computer cache so it doesn't have to redo it.