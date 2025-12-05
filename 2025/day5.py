raw = open("data.txt",'r').read()
_ranges, ids = map(lambda x: x.split('\n'), raw.split('\n\n'))

def add_new_window(windows, new_window):
    windows.append(new_window)
    windows.sort()

    # new list of merged windows
    merged = [windows[0]]

    # since the windows are sorted (by start) we can just compare with previous
    for curr in windows:
        prev = merged[-1]
        if curr[0] <= prev[1]:
            # update previous window end
            # note: no need to update prev window start, since windows are sorted
            prev[1] = max(prev[1], curr[1])
        else:
            merged.append(curr)

    return merged

windows = []
for r in _ranges:
    s,e = list(map(int, r.split('-')))
    
    if not windows:
        windows.append([s,e])
        continue

    windows = add_new_window(windows, [s,e])

score = 0

##part1
# for _id in ids:
#     id = int(_id)
#     for ws,we in windows:
#         if ws <= id <= we:
#             score += 1
#             break

##part2
for ws, we in windows:
    score += we-ws+1

print(score)
