import numpy as np


# make grid, search for X, check all around for MAS
def ceres_search():
    found = 0
    file = open('day4.txt')
    grid = [line.strip() for line in file.readlines()]
    # part 1
    # for y in range(len(grid)):
    #     for x in range(len(grid[0])):
    #         if grid[y][x] == 'X':
    #             found += check(grid, y, x)
    # part 2
    for y in range(1, len(grid)-1):
        for x in range(1, len(grid[0])-1):
            if grid[y][x] == 'A':
                found += check(grid, y, x)
    print(found)


# part 2
def check(grid, y, x):
    valid = 0
    # M . .
    # . A .
    # . . S
    if grid[y-1][x-1] == 'M' and grid[y+1][x+1] == 'S':
        if grid[y+1][x-1] == 'M' and grid[y-1][x+1] == 'S': valid = 1
        elif grid[y+1][x-1] == 'S' and grid[y-1][x+1] == 'M': valid = 1
    # S . .
    # . A .
    # . . M
    elif grid[y-1][x-1] == 'S' and grid[y+1][x+1] == 'M':
        if grid[y+1][x-1] == 'M' and grid[y-1][x+1] == 'S': valid = 1
        elif grid[y+1][x-1] == 'S' and grid[y-1][x+1] == 'M': valid = 1
    return valid

# part 1
# given grid and coord of X, check around
# def check(grid, y, x):
#     count = 0
#     # RIGHT
#     if x < len(grid[0])-3:
#         if grid[y][x+1] == 'M' and grid[y][x+2] == 'A' and grid[y][x+3] == 'S': count+=1
#     # LEFT
#     if x > 2:
#         if grid[y][x-3] == 'S' and grid[y][x-2] == 'A' and grid[y][x-1] == 'M': count += 1
#     # TOP
#     if y > 2:
#         if grid[y-3][x] == 'S' and grid[y-2][x] == 'A' and grid[y-1][x] == 'M': count += 1
#         # DIAG UP RIGHT
#         if x < len(grid[0])-3:
#             if grid[y - 1][x + 1] == 'M' and grid[y - 2][x + 2] == 'A' and grid[y - 3][x + 3] == 'S': count += 1
#         # DIAG UP LEFT
#         if x > 2:
#             if grid[y - 1][x - 1] == 'M' and grid[y - 2][x - 2] == 'A' and grid[y - 3][x - 3] == 'S': count += 1
#     # DOWN
#     if y < len(grid)-3:
#         if grid[y+1][x] == 'M' and grid[y+2][x] == 'A' and grid[y+3][x] == 'S': count += 1
#         # DIAG DOWN RIGHT
#         if x < len(grid[0]) - 3:
#             if grid[y + 1][x + 1] == 'M' and grid[y + 2][x + 2] == 'A' and grid[y + 3][x + 3] == 'S': count += 1
#         # DIAG DOWN LEFT
#         if x > 2:
#            if grid[y+1][x-1] == 'M' and grid[y+2][x-2] == 'A' and grid[y+3][x-3] == 'S': count += 1
#     return count


# part 2
