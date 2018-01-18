import sys

n = input("Enter Colleen's age: ")
candles = []
for x in range(n):
    candles.append(input())
print candles.count(max(candles))