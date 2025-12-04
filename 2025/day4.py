raw = open("/home/joao/advent/2025/data.txt",'r').read().split('\n')

grid = [list(r) for r in raw]
HEIGHT, WIDTH = len(grid), len(grid[0])


def count_rolls(r,c,grid):
    steps = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
    count = 0
    for step in steps:
        newr, newc = r+step[0], c+step[1]
        if newr < 0 or newr > HEIGHT-1 or newc < 0 or newc > WIDTH-1:
            continue
        elif grid[newr][newc] == "@":
            count += 1
    
    return count

def remove_rolls(grid):
    removable_rolls = get_removable_rolls(grid)
    newgrid = grid

    for rollr, rollc in removable_rolls:
        newgrid[rollr][rollc] = '.'

    return newgrid, len(removable_rolls)

def get_removable_rolls(grid):
    removable_rolls = set()
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if grid[r][c] == "@":
                if count_rolls(r,c, grid) < 4:
                    removable_rolls.add((r,c))
    return removable_rolls
                    


newgrid, n_removed_rolls = remove_rolls(grid)
score = n_removed_rolls
##Part1: 
# print(score)


##part2:
while n_removed_rolls != 0:
    newgrid, n_removed_rolls = remove_rolls(newgrid)
    score += n_removed_rolls

print(score)