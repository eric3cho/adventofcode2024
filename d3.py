import re

# parse text file for 'mul(x, y)' form and sum products
def mull_it_over():
    file = open('day3.txt')
    total = 0
    store = []
    do = True
    for line in file:
        store.extend(re.findall(r'mul\(\d{1,3},\d{1,3}\)|do|don\'t', line))
    print(store)



    # # go through store checking for ( , )
    # for match in store:
    #     start = match.find('(')
    #     end = match.find(')')
    #     if start < end and ',' in match[start:end]:
    #         vals = match[start+1:end].split(',')
    #         a = vals[0]
    #         b = vals[1]
    #         if a.isdigit() and b.isdigit():
    #             total += int(a)*int(b)
    # print(total)
