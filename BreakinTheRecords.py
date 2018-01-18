import sys

# n = 9
n = 10
# s = [10, 5, 20, 20, 4, 5, 2, 25, 1]
s = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]

countMin = 0
countMax = 0
maxi = s[0]
mini = s[0]
j = 1
for i in range(len(s)):
    if(s[j] > maxi):
        maxi = s[j]
        countMax += 1
    elif(s[j] < mini):
        mini = s[j]
        countMin += 1
    if(j < n-1):
        j += 1

# temp = []
# temp.append(s[0])
# countMin = 0
# countMax = 0
# for i in range(0,len(s)-1):
#     temp.append(s[i])
#     mini = min(temp)
#     maxi = max(temp)
#     store = s[i+1]
#     if(store < mini):
#         countMin += 1
#     elif(store > maxi):
#         countMax += 1

print (str(countMax) + " " + str(countMin))