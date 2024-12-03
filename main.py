import numpy as np

file = open('day1.txt', 'r')
left = []
right = []
for line in file:
    clean = line.split()
    left.append(int(clean[0]))
    right.append(int(clean[1]))
left = np.sort(np.array(left))
right = np.sort(np.array(right))
total = 0
for x in range(len(left)):
    total += np.abs(left[x] - right[x])
print(total)
