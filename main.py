import numpy as np


# day 1
def abs_diff():
    file = open('day1.txt')
    left = []
    right = []
    for line in file:
        clean = line.split()  # creates array of strings
        left.append(int(clean[0]))  # cast as int, add to list
        right.append(int(clean[1]))
    left = np.sort(left)
    right = np.sort(right)
    print(np.sum(np.abs(left - right)))


abs_diff()

