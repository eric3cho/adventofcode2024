import numpy as np


# weight each left id by its occurrence and sum
def weighted_count():
    # setup
    file = open('day1.txt')
    left = []
    right = []
    for line in file:
        clean = line.split()  # creates array of strings
        left.append(int(clean[0]))  # cast as int, add to list
        right.append(int(clean[1]))
    left = np.sort(left)
    right = np.sort(right)

    total = 0
    left = left.tolist()
    right = right.tolist()
    for x in left:
        total += (x * right.count(x))
    print(total)
