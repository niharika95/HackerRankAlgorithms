import sys

n = 6
ar = [1, 3, 2, 6, 1, 2]
k = 3

flag = 0
for i in range(len(ar)-1):
    for j in range(i+1, len(ar)):
        temp = ar[i]+ar[j]
        if temp % k == 0:
            flag += 1

print flag