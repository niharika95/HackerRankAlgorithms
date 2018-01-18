import sys

n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

c ={}
flag = 0

for i in ar:
    if i in c.keys():
        c[i] += 1
    else:
        c[i] = 1

for key,value in c.iteritems():
    if (value % 2 == 0):
        flag += value/2
    else:
        temp = value/2
        flag += temp

print flag
