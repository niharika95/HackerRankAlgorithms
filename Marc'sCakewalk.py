import sys

n = 3
c = [1, 3, 2]
miles = 0

for i in range(n):
    miles += pow(2,(i+1)) * c[i]