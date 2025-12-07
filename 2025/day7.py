raw = open("data.txt", 'r').read()


data = raw.split("\n")
start = (0, (len(data[0])-1) //2)


##part1
# beams = [start]
# seen = set()
# score = 0
# beamsplitscore = 0
# while beams:
#     beam = beams.pop(0)

#     if beam not in seen:
#         seen.add(beam)
#     else:
#         continue
#     if beam[0] == len(data)-1:
#         score += 1
#         continue

#     if data[beam[0]][beam[1]] == "^":
#         beamsplitscore += 1
#         new_beam1 = (beam[0], beam[1]+1)
#         new_beam2 = (beam[0], beam[1]-1)
#         beams.append(new_beam1)
#         beams.append(new_beam2)
#         continue

#     beams.append((beam[0]+1, beam[1]))

# print(beamsplitscore)





##part2
seen_paths = dict()
def get_path(r,c):
    if (r,c) in seen_paths:
        return seen_paths[(r,c)]

    while r < len(data) and data[r][c] != "^":
        r += 1 

    if r == len(data):
        return 1
    
    if (r,c) in seen_paths:
        return seen_paths[(r,c)]
    
    seen_paths[(r,c)] = 0
    if c > 0:
        seen_paths[(r,c)] += get_path(r,c-1)
    if c < len(data[0])-1:
        seen_paths[(r,c)] += get_path(r,c+1)

    return seen_paths[(r,c)]

print(get_path(*start))

    
    
