import sys

n = input("Enter the number of integers: ")
li = []
pos = []
neg = []
zero = []

for x in range(n):
    li.append(input())

for x in range(n):
    if(li[x] > 0):
        pos.append(li[x])
    elif(li[x] < 0):
        neg.append(li[x])
    else:
        zero.append(li[x])

print ("{0:.6f}".format(float(len(pos)) / float (n)))
print ("{0:.6f}".format(float(len(neg)) / float (n)))
print ("{0:.6f}".format(float(len(zero)) / float (n)))