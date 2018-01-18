import sys

n = 6
arr = [4,6,5,3,3,1]
store = []
for i in range(n):
    temp = []
    ('store'+str(i)) = temp
    for j in range(i+1,n-1):
        if (abs(arr[i] - arr[j] <= 1 )):
            if arr[i] not in store:


