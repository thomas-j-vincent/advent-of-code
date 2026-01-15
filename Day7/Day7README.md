# Day 7

## Task 1:

On Day 7 we find ourself in the teleportation room! However, the teleporter seems to be broken and we need to fix it. According to the manual there is an issue with one of the **tachyon manifolds** they work as follows: 
A beam starts from the position **S**, always moving downwards. They pass freely through empty space (.) however if there is a splitter (^) the beam at that position stops and "splits" to the immediate right and immediate left of it. We need to calculate the amount of times our beam gets split.

My initial approach was to render the program as you would if you were doing it by hand however, this was very resource intensive and had no way of stopping the beam continuing from the splitter- it would render next to it but then continue on its path in the next row. To solve this I started following a youtube video by HyperNeutrino. 

 ## Explaining the code top to bottom:##

