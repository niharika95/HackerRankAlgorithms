import sys

n = 4
spaceSymbol = ' '
hashSymbol = '#'
spaceCounter = n-1
for i in range(1,n+1):
    print (spaceSymbol*(spaceCounter) + hashSymbol*i)
    spaceCounter-=1