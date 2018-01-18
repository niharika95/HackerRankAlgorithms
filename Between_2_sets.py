#!/bin/python3
import sys


# if __name__ == "__main__":
#     n, m = input().strip().split(' ')
#     n, m = [int(n), int(m)]
#     a = list(map(int, input().strip().split(' ')))
#     b = list(map(int, input().strip().split(' ')))
#     total = getTotalX(a, b)
#     print(total)

n = 2
m = 3
a = [2, 4]
b = [16, 32, 96]

finalCount = 0

for i in range(1, max(b)):
    flag1 = 0
    flag2 = 0
    for j in range(len(a)):
        if(i % a[j] == 0):
            flag1 += 1

    if flag1 == len(a):
        for k in range(len(b)):
            if(b[k] % i == 0):
                flag2 += 1

    if flag2 == len(b):
        finalCount += 1

print finalCount