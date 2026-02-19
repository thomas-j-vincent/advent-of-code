from functools import cache 
graph = {}

with open("Day11Input.txt", "r") as file:
    for line in file:
        input, outputs = line.strip().split(": ")
        graph[input] = outputs.split()

@cache
def count(input, output):
    if input == output: return 1
    return sum(count(x, output) for x in graph.get(input, []))

print(count("svr", "dac")* count("dac", "fft")* count("fft", "out")\
        + count("svr", "fft") * count("fft", "dac") * count("dac", "out")
)