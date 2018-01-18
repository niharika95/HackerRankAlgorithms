# A = []
# B = []
#
# print ("Enter the scores for A:\n")
# for i in range(0,3):
#     A.append(input())
#
# print ("Enter the scores for B:\n")
# for i in range(0,3):
#     B.append(input())



def solve(a0, a1, a2, b0, b1, b2):
    aResult = 0
    bResult = 0

    if a0<b0:
        bResult = bResult + 1
    elif a0>b0:
        aResult = aResult +1

    if a1<b1:
        bResult = bResult + 1
    elif a1>b1:
        aResult = aResult +1

    if a2<b2:
        bResult = bResult + 1
    elif a2>b2:
        aResult = aResult +1

    print (str(aResult) + "  " + str(bResult))

solve(5,6,7,3,6,10)