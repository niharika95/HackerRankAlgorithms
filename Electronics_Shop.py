import sys

s = 5
n = 1
m = 1

keyboards = [4]
drives = [5]

addition = []

for i in range(len(keyboards)):
    for j in range(len(drives)):
        temp = keyboards[i] + drives[j]
        if temp <= s:
            addition.append(temp)

if len(addition) > 0:
    print max(addition)
else:
    print -1