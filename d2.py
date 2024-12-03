import numpy as np


# weight each left id by its occurrence and sum
def rednosed_reports():
    file = open('day2.txt')
    safe = 0
    for line in file:
        levels = [int(num) for num in line.split()]
        if valid(levels):
            if levels == sorted(levels) or levels == sorted(levels, reverse=True): safe += 1
    print(safe)


# check if distance between all list elements are within range
# part 2, one exception allowed
def valid(nums):
    errors = 0
    for x in range(len(nums) - 1):
        if abs(nums[x] - nums[x + 1]) > 3 or abs(nums[x] - nums[x + 1]) < 1: errors += 1
        if errors > 1: return False
    return True
