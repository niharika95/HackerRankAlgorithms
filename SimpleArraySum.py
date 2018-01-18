n = int(raw_input("Enter n: "))
ar = []

def takeInput():
    print ("Enter the elements: \n")
    for i in range (0,n):
        ar.append(int(raw_input()))

def solve(n, ar):
    return sum(ar)

takeInput()
print (solve(n, ar))
