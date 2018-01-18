import sys

q = 3
x = 2
y = 1
z = 3

for i in range(q):
    if (abs(x-z) < abs(y-z)):
        print 'Cat A'
    elif (abs(x-z) > abs(y-z)):
        print 'Cat B'
    elif (abs(x-z) == abs(y-z)):
        print 'Mouse C'