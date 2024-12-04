import re


def mull_it_over():
    file = open('day3.txt')
    total = 0
    store = []
    # search every line for matches to 'mul'
    # slice max possible segment and add to store
    for line in file:
        # get start of all matches in line
        indices = [match.start() for match in re.finditer('mul', line)]
        for i in indices:
            store.append(line[i+3:i+12])
    for x in store:
        for