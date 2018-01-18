import sys

n = 4
k = 1
ar = [3, 10, 2, 9]
b = 7

total = sum(ar)
total -= ar[k]
eachTotal = int(total/2)
if (eachTotal == b):
    print 'Bon Appetit'
else:
    print (b - eachTotal)