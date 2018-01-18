import sys

n = 5
s = [1, 2, 1, 3, 2]
d = 3
m = 2

flag = 0
if (n == 1):
    for i in range(n):
        total = 0
        for j in range(i,i+m):
            total += s[j]
        if (total == d):
            flag += 1

if(n > 1):
    for i in range(n-1):
        total = 0
        for j in range(i,i+m):
            total += s[j]
        if (total == d):
            flag += 1

print flag