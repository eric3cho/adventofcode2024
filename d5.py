def print_queue():
    # check if both nums exist, skip rules if not
    # assign index to both nums to check if in order
    rules_file = open('day5rules.txt')
    rules = [line.strip().split('|') for line in rules_file]
    update_file = open('day5updates.txt')
    update = [line.strip().split(',') for line in update_file]
    sum = 0

    for line in update.readlines():
        sum += check(line, rules)


# will return mid if passes rules, will return 0 otherwise
def check(line, rules):
    # sort valid rules
    for rule in rules:
        if all(num in line for num in rule):
