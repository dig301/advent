raw = open("data.txt", 'r').read()

lines = []
for l in raw.split('\n'):
    lines.append([int(n) for n in l.split(' ')])
score = 0

def is_ok(line):
    inc = line[0] < line[1]
    N = len(line)

    for n in range(N-1):
        if (line[n] < line[n+1]) == inc and (1<=abs(line[n]-line[n+1])<=3):
            continue
        return False
    return True

##part1
# for l in lines:
#     if is_ok(l):
#         score += 1
#
# print(score)
# 


##part2
for l in lines:
    if is_ok(l):
        score += 1
        continue
    
    for index in range(len(l)):
        if is_ok(l[:index] + l[index+1:]):
            score += 1
            break

print(score)
        
