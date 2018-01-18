def aVeryBigSum(n, ar):
    sum = 0
    print ("Debug 3")
    for i in range(0,n):
        summ = summ + ar[i]
    print ("Debug 4")
    return summ

print "Hello"
n = int(input().strip())
print ("Hello")
ar = list(map(int, input().strip().split(' ')))
print ("Debug 1")
# ar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
# print ("Debug 2")
# result = aVeryBigSum(5, ar)
# print ("Debug 5")
# print(result)
# print ("Debug 6")