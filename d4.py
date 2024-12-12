import numpy as np


# make grid, search for X, check all around for MAS
def ceres_search():
    found = 0
    file = open('day4.txt')
    lines = [line.strip() for line in file.readlines()]
    grid = np.array(lines)
    for y in range(len(grid[0])):
        for x in range(y):
            if grid[y][x] == 'X':
                found += check(grid, y, x)
    print(found)


# given grid and coords of X, check around
def check(grid, y, x):
    count = 0
    # RIGHT
    if x < len(grid[0])-2:  # at least 7
        if grid[y, x+1:x+4] == 'MAS': count+=1
    # LEFT
    if x > 2:   # at least 3
        if grid[y, x-3:x] == 'SAM': count+=1
    # TOP
    if y > 2:
        if grid[y-3:y, x] == 'SAM': count+=1
        # DIAG UP RIGHT
        if x < len(grid[0])-2:
            if grid[y - 1][x + 1] == 'M' and grid[y - 2][x + 2] == 'A' and grid[y - 3][x + 3] == 'S': count += 1
        # DIAG UP LEFT
        if x > 2:
            if grid[y - 1][x - 1] == 'M' and grid[y - 2][x - 2] == 'A' and grid[y - 3][x - 3] == 'S': count += 1
    # DOWN
    if y < len(grid)-2:
        if grid[y+1:y+4, x] == 'MAS': count+=1
        # DIAG DOWN RIGHT
        if x < len(grid[0]) - 2:
            if grid[y + 1][x + 1] == 'M' and grid[y - 2][x + 2] == 'A' and grid[y - 3][x + 3] == 'S': count += 1
        # DIAG DOWN LEFT
        if x > 2:
           if grid[y+1][x-1] == 'M' and grid[y+2][x-2] == 'A' and grid[y+3][x-3] == 'S': count += 1
    return count