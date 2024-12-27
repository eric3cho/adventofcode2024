import numpy as np


# make grid, search for X, check all around for MAS
def ceres_search():
    found = 0
    file = open('day4.txt')
    grid = [line.strip() for line in file.readlines()]
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'X':
                found += check(grid, y, x)
    print(found)


# given grid and coord of X, check around
def check(grid, y, x):
    count = 0
    # RIGHT
    if x < len(grid[0])-2:
        if grid[y][x+1] == 'M' and grid[y][x+2] == 'A' and grid[y][x+3] == 'S': count+=1
    # LEFT
    if x > 2:
        if grid[y][x-3] == 'S' and grid[y][x-2] == 'A' and grid[y][x-1] == 'M': count += 1
    # TOP
    if y > 2:
        if grid[y-3][x] == 'S' and grid[y-2][x] == 'A' and grid[y-1][x] == 'M': count += 1
        # DIAG UP RIGHT
        if x < len(grid[0])-2:
            if grid[y - 1][x + 1] == 'M' and grid[y - 2][x + 2] == 'A' and grid[y - 3][x + 3] == 'S': count += 1
        # DIAG UP LEFT
        if x > 2:
            if grid[y - 1][x - 1] == 'M' and grid[y - 2][x - 2] == 'A' and grid[y - 3][x - 3] == 'S': count += 1
    # DOWN
    if y < len(grid)-3:
        if grid[y+1][x] == 'M' and grid[y+2][x] == 'A' and grid[y+3][x] == 'S': count += 1
        # DIAG DOWN RIGHT
        if x < len(grid[0]) - 3:
            if grid[y + 1][x + 1] == 'M' and grid[y + 2][x + 2] == 'A' and grid[y + 3][x + 3] == 'S': count += 1
        # DIAG DOWN LEFT
        if x > 2:
           if grid[y+1][x-1] == 'M' and grid[y+2][x-2] == 'A' and grid[y+3][x-3] == 'S': count += 1
    return count