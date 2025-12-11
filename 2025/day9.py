import itertools
from collections import defaultdict

raw = open("data.txt", 'r').read()

tiles = [tuple(map(int, a.split(","))) for a in raw.split("\n")]



##part1
# combs = itertools.combinations(tiles, 2)
# max_area = 0
# for c in combs:
#     tile_a, tile_b = c
#     area = abs((tile_a[0] - tile_b[0] + 1) * (tile_a[1] - tile_b[1] + 1))

#     max_area = max(max_area, area)



##part2
# get edge tiles and mapping of edges by row
edge_tiles = set()
edges_by_row = dict()
n = len(tiles)
for i in range(n):
    x1, y1 = tiles[i]
    x2, y2 = tiles[(i + 1) % n]
    if x1 == x2:  # vertical
        for y in range(min(y1, y2), max(y1, y2) + 1):
            edge_tiles.add((x1, y))
            edges_by_row.setdefault(y, set()).add(x1)
    elif y1 == y2:  # horizontal
        for x in range(min(x1, x2), max(x1, x2) + 1):
            edge_tiles.add((x, y1))
            edges_by_row.setdefault(y1, set()).add(x)
    else:
        raise ValueError("edges must be horizontal or vertical")
    
# convert edge positions to sorted ranges by row
edge_ranges_by_row = dict()
for y, xs_set in edges_by_row.items():
    if not xs_set:
        continue

    ranges = []
    xs = sorted(xs_set)
    start = xs[0]
    end = xs[0]
    for v in xs[1:]:
        if v == end + 1:
            end = v
        else:
            ranges.append((start, end))
            start = v
            end = v
    ranges.append((start,end))
    edge_ranges_by_row[y] = ranges


minx = min(x for x,_ in tiles)
maxx = max(x for x,_ in tiles)
miny = min(y for _,y in tiles)
maxy = max(y for _,y in tiles)


def x_in_ranges(x, ranges):
    low = 0
    high = len(ranges)-1
    while low <= high:
        middle = (low+high)//2
        s,e = ranges[middle]
        if x<s:
            high = middle-1
        elif x>e:
            low = middle+1
        else:
            return True
    return False

# get max horizontal segments per row
row_max_segments = {}
for y, ranges in edge_ranges_by_row.items():
    start = min(s for s,_ in ranges)
    end = max(e for _,e in ranges)
    row_max_segments[y] = [(start, end)]

def row_contains_segment(y, start_x, end_x):
    #check if a horizontal segment is fully inside a row
    seg = row_max_segments.get(y)
    if not seg:
        return False
    s, e = seg[0]  # only one segment per row
    return s <= start_x and end_x <= e
    

max_area = 0
for r1, r2 in itertools.combinations(tiles, 2):
    x1, y1 = r1
    x2, y2 = r2

    minx, maxx = min(x1, x2), max(x1, x2)
    miny, maxy = min(y1, y2), max(y1, y2)
    area = (maxx - minx + 1) * (maxy - miny + 1)
    if area < max_area:
        continue

    # check top/bottom edges by row
    valid = True
    for y in [miny, maxy]:
        if not row_contains_segment(y, minx, maxx):
            valid = False
            break
    if not valid:
        continue

    # check left/right edges by row
    for x in [minx, maxx]:
        for y in range(miny, maxy+1):
            if not row_contains_segment(y, x, x):
                valid = False
                break
        if not valid:
            break

    if valid:
        max_area = max(max_area, area)

print(max_area)