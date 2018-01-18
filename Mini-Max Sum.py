import sys

arr = []
print "Enter 5 positive integers:"
for i in range(5):
    arr.append(input())
arr.sort()
min = 0
for i in range(4):
    min = min + arr[i]

arr.reverse()
maxi = 0
for i in range(4):
    maxi = maxi + arr[i]

# print ("Max: " + str(maxi))
# print ("Min: " + str(min))

print (min + " " + maxi)
