import re

# parse text file for 'mul(x, y)' form and sum products
def mull_it_over():
    file = open('day3.txt')
    total = 0
    store = []
    # search every line for matches to 'mul', slice by max possible size and add to store
    for line in file:
        # get start of all matches in line
        indices = [match.start() for match in re.finditer('mul', line)]
        # get the chunks after mul into store
        for i in indices:
            store.append(line[i+3:i+12])
    # go through store checking for ( , )
    for match in store:
        start = match.find('(')
        end = match.find(')')
        if start < end and ',' in match[start:end]:
            vals = match[start+1:end].split(',')
            a = vals[0]
            b = vals[1]
            if a.isdigit() and b.isdigit():
                total += int(a)*int(b)
    print(total)
