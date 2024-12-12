import re

# parse text file for 'mul(x, y)' form and sum products
def mull_it_over():
    file = open('day3.txt')
    total = 0
    store = []
    do = True

    for line in file:
        print(line)
        # put don't first because do overlaps
        # alternatively, search for "do(" or "don't("
        store.extend(re.findall(r"mul\(\d{1,3},\d{1,3}\)|don't|do", line))
    for match in store:
        if match == 'don\'t': do = False
        elif match == 'do': do = True
        else:
            if do:
                nums = re.findall(r"(\d+)", match)
                total += int(nums[0]) * int(nums[1])
    print(total)
    file.close()
