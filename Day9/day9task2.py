# Day9B - coordinate compression, matrix approach.
import pandas as pd
import numpy as np

D9 = pd.read_csv('day9inputtedvalues.txt', header=None)

unique = np.unique(D9[[0, 1]])
factors = np.arange(len(unique))

D9[[0, 1]] = D9[[0, 1]].replace(unique, factors)

x = list(D9[0])
y = list(D9[1])

s = np.zeros((max(y)+1, max(x)+1), dtype=np.uint8)

for i in range(len(D9)):
    s[y[i]][x[i]] = 1

for i in range(len(D9)):
    for j in range(len(D9)):
        if i != j:
            if x[i] == x[j]:
                for k in range(y[i], y[j]+1):
                    s[k][x[i]] = 1
            if y[i] == y[j]:
                for k in range(x[i], x[j]+1):
                    s[y[i]][k] = 1

for i in range(len(s)):
    border = []
    for j in range(s.shape[1]):
        if s[i][j] != 0:
            border.append(j)
    if len(border) >= 2:
        for j in range(min(border), max(border) + 1):
            if s[i][j] == 0:
                s[i][j] = 1
m = []

for i in range(len(D9)):
    for j in range(i+1, len(D9)):
        x2 = max(x[i], x[j])
        y2 = max(y[i], y[j])
        x1 = min(x[i], x[j])
        y1 = min(y[i], y[j])
        
        if x1 == x2 or y1 == y2:
            continue
            
        n = (1 + unique[x2] - unique[x1]) * (1 + unique[y2] -unique[y1])
        m.append((x1,y1,x2,y2,n))

m = sorted(m, key=lambda x:x[-1], reverse = True)

p1 = max(m[:][4])

for i in range(len(m)):
    r = [row[m[i][0]:m[i][2]+1] for row in s[m[i][1]:m[i][3]+1]]
    if any(0 in j for j in r):
        continue
    else:
        p2 = m[i][4]
        break

print(p1,p2)