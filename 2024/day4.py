raw = open("data.txt", 'r').read()

grid = [list(l) for l in raw.split("\n")]

HEIGHT, WIDTH = len(grid), len(grid[0])

##part1
# def count_xmas(r,c):
#     dirs = [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1)]
#     word = 'XMAS'
#     score = 0
  
#     for dr, dc in dirs:
#         count = 0
#         for i in range(1,4):
#             nr, nc = r+dr*i, c+dc*i
#             if 0 <= nr <= HEIGHT-1 and 0 <= nc <= WIDTH-1 and grid[nr][nc] == word[i]:
#                 count += 1
#         if count == 3:
#             score += 1
    
#     return score

# score = 0
# for r,l in enumerate(raw.split("\n")):
#     for c, val in enumerate(l):
#         if grid[r][c] == 'X':
#             score += count_xmas(r,c)


##part2
def count_xmas(r,c):
    dirs = [(1,1), (-1,1)]
    word = 'MS'
  
    count = 0
    for dr, dc in dirs:
        nr1, nc1, nr2, nc2 = r+dr, c+dc, r-dr, c-dc
        if 0 <= nr1 <= HEIGHT-1 and 0 <= nc1 <= WIDTH-1 and 0 <= nr2 <= HEIGHT-1 and 0 <= nc2 <= WIDTH-1:
            if grid[nr1][nc1] in word and grid[nr2][nc2] in word and grid[nr1][nc1] != grid[nr2][nc2]:
                count += 1
        if count == 2:
            return 1
    
    return 0

score = 0
for r,l in enumerate(raw.split("\n")):
    for c, val in enumerate(l):
        if grid[r][c] == 'A':
            score += count_xmas(r,c)

print(score)