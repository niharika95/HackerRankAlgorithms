import sys

n = 8
steps = 'UDDDUDUU'

s = list(steps)
flag = 0

for i in range(len(s)):
    if s[i] == 'D':
        flag += 1

print flag