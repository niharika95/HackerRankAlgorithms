import sys

x1 = 0
v1 = 3
x2 = 4
v2 = 2
x1List = []
x2List = []

x1new = x1
x2new = x2


for x in range(-1,10001):
    if(10001 > (x1new + v1)):
        x1new += v1
        x1List.append(x1new)

for x in range(-1,10001):
    if(10001 > (x2new + v2)):
        x2new += v2
        x2List.append(x2new)

flag = 0

for i in range(min(len(x1List),len(x2List))):
    if(x1List[i] == x2List[i]):
        flag = 1
        break
    else:
        flag = 0

if (flag == 1):
    print 'YES'
else:
    print 'NO'

print x1List
print '\n'
print x2List