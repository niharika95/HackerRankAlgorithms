import sys

# s,t = input().strip().split(' ')
# s,t = [int(s),int(t)]
# a,b = input().strip().split(' ')
# a,b = [int(a),int(b)]
# m,n = input().strip().split(' ')
# m,n = [int(m),int(n)]
# apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
# orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

a = 5
b = 15
s = 7
t = 11
m = 3
n = 2
apple = [-2, 2, 1]
appleDist = []
orange = [5, -6]
orangeDist = []
appleCount = 0
orangeCount = 0

for i in range(len(apple)):
    appleDist.append(int(a + apple[i]))

for i in range(len(orange)):
    orangeDist.append(int(b + orange[i]))

for i in range(m):
    if(appleDist[i] > a):
        if (appleDist[i]>=s and appleDist[i]<=t):
            appleCount += 1

for i in range(n):
    if(orangeDist[i] < b):
        if (orangeDist[i]>=s and orangeDist[i]<=t):
            orangeCount += 1

print ("Apple Count: " + str(appleCount))
print ("Orange Count: " + str(orangeCount))