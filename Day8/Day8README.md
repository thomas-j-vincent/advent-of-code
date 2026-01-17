# Day 7

## Task 1: ##

On day 8 we need to use euclidean distance to help some elves connect electrical junction boxes so they can form an light installation. Having connected the closest 1000 pairs of junction boxes we need to multiply the size of the three largest circuits to get our puzzle answer.

 ### Explaining the code top to bottom:###

We first import the math module so we can calculate the euclidean distance between the junction boxes. 
Having opened the file we split it into lines and then split the lines on commas to get the three coordinate components, we then convert those values into integers so they can be properly treated as numbers before putting them in a list. This results in a list where each entry is one set of coordinates.
edges is every possible two-box combination of connections, it ensures the first value is smaller than the second value by iterating through incrementally from the start instead of randomly- removing the chance for duplicates.
With ``edges.sort(key=lambda x: math.hypot(*[a - b for a, b in zip(boxes[x[0]], boxes[x[1]])]))``We sort the edges into the shortest distance 

**Disjoint sets** are used to join the circuits together and also to identify if they have been already joined. They are a data structure whereby we have a bunch of objects, each contained within a set, and each set is disjointed (they are not connected). These are usually implimented as a graph or a set of trees where one of the objects is the parent of the tree and each of the other objects are branches off the tree. This enables us to merge one tree into another. 

In this program we first store the "parent" of the node tree (initially just the node itself):

The root function enables us to find the parent of the tree from any node within the tree.

To merge the trees together we use the merge function, first by finding the parent of the first tree, and then putting it into the second tree, making the second parent the parent of all of them.

We then merge the first 1000 shortest connections by cutting off the edges list after 1000 and then merging each of the values in that list. To determine the sizes we look at a junction box, find the set it is in (by finding the root), and then increase the size of the set. We sort this in reverse to get the largest sets, and then multiply the first values by each other to get our answer. Which is then printed.

### Maximising efficiency: ###

As the root function goes up one layer at a time, this could lead to long processing times if we end up with a massive tree. To solve this we use path compression so that we do not have to go through many "branches" to get to the parent, essentially making the tree linear. This is done in the line ``parent[x] = root(parent[x])``. This also impacts the merging as we do not want to move a merged tree to a child of the descendent of the parent, we want to make it the root of the second tree (``parent[root(a)] = root(b)`` **not** ``parent[root(a)] = b``). Finally we ***could*** find the deepest tree, and put the shallower tree a child of the deeper issue however, we do not do this as path compression already *mostly* solves this problem. 

## Task 2: ##

In part two we need to carry on going until we have connected all of the junction boxes, and once they are all connected we take the last two junction boxes that we connected. And then multiply them.

 ### Explaining the code top to bottom:###

The code is very similar to the last program we used however, instead of looping through the first 1000 shortest connections.
To identify when we are done we create a circuit variable, that is initially just the length of boxes
each time we check if the root of each circuit is equal to the root of the second circuit, as if they are equal they are already in the same circuit and the merge function can be skipped. If they are not in the same function we merge together and decrease the number of circuits by one (as we have turned two connections into one)
We continue this loop until the number of circuits is 1 at which point we print the result of x coordinate box a * x coordinate box b. 
we then break out of the loop.

### Maximising efficiency: ###

There are no optimisations for the second code.