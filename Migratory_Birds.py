import sys

n = 6
ar = [1, 4, 4, 4, 5, 3]

birds = {}
temp = []

for i in ar:
    if i in birds.keys():
        birds[i] += 1
    else:
        birds[i] = 1

for key, value in birds.iteritems():
    if value == max(birds.values()):
        temp.append(key)

print min(temp)
