import re

# parse text file for 'mul(x, y)' form and sum products
def mull_it_over():
    file = open('day3.txt')
    total = 0
    do = True
    # search every line for matches to 'mul', slice by max possible size and add to store
    seq = 'mul\(\d{1,3},\d{1,3}\)'
    store = re.finditer(r'seq|do|don\'t', file)
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
