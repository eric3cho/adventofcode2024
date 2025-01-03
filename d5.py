def print_queue():
    # check if both nums exist, skip rules if not
    # assign index to both nums to check if in order
    rules_file = open('day5rules.txt')
    rules = [line.strip().split('|') for line in rules_file]
    update_file = open('day5updates.txt')
    update = [line.strip().split(',') for line in update_file]
    sum = 0

    for line in update:
        sum += check(line, rules)

    print(sum)


# pt 2: fix invalid and return mid
def check(line, rules):
    mid = 0
    valid = [rule for rule in rules if all(num in line for num in rule)]
    for rule in valid:
        a = line.index(rule[0])
        b = line.index(rule[1])
        if a > b:
            new = reconstruct(line, valid)
            mid = new[(len(new)-1)//2]
    return int(mid)


# reconstruct with insertion sort
def reconstruct(line, valid):
    new = []
    # go through every val, place and check, if invalid move and check again
    for val in line:
        for i in range(len(line)):
            new.insert(i, val)
            if isvalid(new, valid): break
            else: new.remove(val)
    return new


# check if current line obeys applicable rules
def isvalid(line, valid):
    for rule in valid:
        # only get currently relevant rules
        if all(num in line for num in rule):
            if line.index(rule[0]) > line.index(rule[1]): return False
    return True

# pt 1: will return mid if passes rules, will return 0 otherwise
# def check1(line, rules):
#     mid = 0
#     # sort valid rules
#     # valid = [rule for rule in rules if all(num in line for num in rule)]
#     for rule in rules:
#         # nums in rule are in update
#         if all(num in line for num in rule):
#             if line.index(rule[0]) < line.index(rule[1]): mid = line[(len(line)-1)//2]
#             else:
#                 mid = 0
#                 break
#     return int(mid)