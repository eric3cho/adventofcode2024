import numpy as np


# check int list for conditions and tally safe lists
# pt2: one level exception allowed
def rednosed_reports():
    file = open('day2.txt')
    safe = 0
    maybe = []
    for line in file:
        levels = [int(num) for num in line.split()]
        # first pass for safe, add questionable sequences to maybe
        if valid2(levels) and valid1(levels): safe += 1
        else: maybe.append(levels)
    # second pass of maybe, remove each digit and check valid
    for test in maybe:
        valid = False
        for x in range(len(test)):
            a = test.pop(x)
            if valid1(test) and valid2(test): valid = True
            test.insert(x, a)
        if valid: safe += 1
    print(safe)
    file.close()

# check if distance between all list elements are within range
def valid1(nums):
    for x in range(len(nums) - 1):
        if abs(nums[x] - nums[x + 1]) > 3 or abs(nums[x] - nums[x + 1]) < 1: return False
    return True

# check if all ascending or all descending
def valid2(nums):
    return nums == sorted(nums) or nums == sorted(nums, reverse=True)
