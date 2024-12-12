# make grid, search for X, check all around for MAS
def ceres_search():
    found = 0
    file = open('day4.txt')
    grid = [line.strip() for line in file.readlines()]
    for y in range(len(grid[0])):
        for x in range(y):
            if grid[y][x] == 'X':
                found += check(grid, y, x)
# given grid and coords of X, check around
def check(grid, y, x):
    count = 0
    # right limit
    if x < len(grid[0])-2:
    # right
    if grid[y][x+1:x+4] == 'MAS': count+=1
    # left
    if grid[y][x-3:x] == 'SAM': count+=1
    # top
    if grid[y-3:y][x] == 'SAM': count+=1
    # down
    if grid[y+1:y+4][x] == 'MAS': count+=1
    # diag up right
    if grid[y-1][x+1] == 'M' and grid[y-2][x+2] == 'A' and grid[y-3][x+3] == 'S': count+=1
    # diag up left
    if grid[y-1][x-1] == 'M' and grid[y-2][x-2] == 'A' and grid[y-3][x-3] == 'S': count += 1
    # diag down right
    if grid[y+1][x+1] == 'M' and grid[y-2][x+2] == 'A' and grid[y-3][x+3] == 'S': count += 1
    # diag down left
    if grid[y+1][x-1] == 'M' and grid[y+2][x-2] == 'A' and grid[y+3][x-3] == 'S': count += 1