from functools import cache 
graph = {}

with open("Day11Input.txt", "r") as file:
    for line in file:
        src, dsts = line.strip().split(": ")
        graph[src] = dsts.split()

@cache
def count(src, dst):
    if src == dst: return 1
    return sum(count(x, dst) for x in graph.get(src, []))

print(count("you", "out"))