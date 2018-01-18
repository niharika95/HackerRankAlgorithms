#!/bin/python3

import sys
import numpy as np

ar = []

n = int(input("Enter N: "))
for i in range(n):
	ar.append([])
	for j in range(n):
		ar[i].append(int(input()))
        print ('\n')

print np.matrix(ar)

leftToRight = 0
for i in range(n):
	for j in range(n):
		if i==j:
			leftToRight = int(leftToRight) + int(ar[i][j])

print ('Left to Right: ' + str(leftToRight))

rightToLeft = 0
for i in range(n):
	for j in range(n):
		if(i + j == (n-1)):
			rightToLeft = int(rightToLeft) + int(ar[i][j])

print ('Right To Left: ' + str(rightToLeft))

difference = abs(rightToLeft - leftToRight)
print difference

# n = int(input().strip())
# a = []
# for a_i in range(n):
#     a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
#     a.append(a_t)