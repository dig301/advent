import itertools

raw = open("data.txt").read()

boxes = [tuple(map(int, x.split(","))) for x in raw.split("\n")]
circuits = []

def get_distance(box1, box2):
    return (box2[0]-box1[0])**2 + (box2[1]-box1[1])**2 +(box2[2]-box1[2])**2

ordered_combs = sorted(list(itertools.combinations(boxes, 2)), key=lambda x: get_distance(x[0],x[1]))


##part1
# N=1000
# count = 0
# while count < N-1:
#     box_a, box_b = ordered_combs[count]
#     idx_a = idx_b = None
    
#     for idx, c in enumerate(circuits):
#         if box_a in c:
#             idx_a = idx
#         if box_b in c:
#             idx_b = idx
#         if idx_a is not None and idx_b is not None:
#             break

#     if idx_a is not None and idx_a == idx_b:
#         # they are already included in the same circuit
#         pass

#     elif idx_a is not None and idx_b is not None and idx_a != idx_b:
#         # both in different circuits. must merge them
#         circuits[idx_a].update(circuits[idx_b])
#         circuits.pop(idx_b)
    
#     elif idx_a is not None: # only box_a in a circuit. must add box_b
#         circuits[idx_a].add(box_b)

#     elif idx_b is not None: # only box_b in a circuit. must add box_a
#         circuits[idx_b].add(box_a)
    
#     else:
#         circuits.append({box_a, box_b})

#     count += 1


# sz = sorted([len(c) for c in circuits], reverse=True)
# print(sz[0] * sz[1] * sz[2])


##part2
count = 1
circuits.append({*ordered_combs[0]})
while len(circuits) != 1 or len(circuits[0]) != len(boxes):
    box_a, box_b = ordered_combs[count]
    idx_a = idx_b = None
    
    for idx, c in enumerate(circuits):
        if box_a in c:
            idx_a = idx
        if box_b in c:
            idx_b = idx
        if idx_a is not None and idx_b is not None:
            break

    if idx_a is not None and idx_a == idx_b:
        # they are already included in the same circuit
        pass

    elif idx_a is not None and idx_b is not None and idx_a != idx_b:
        # both in different circuits. must merge them
        circuits[idx_a].update(circuits[idx_b])
        circuits.pop(idx_b)
    
    elif idx_a is not None: # only box_a in a circuit. must add box_b
        circuits[idx_a].add(box_b)

    elif idx_b is not None: # only box_b in a circuit. must add box_a
        circuits[idx_b].add(box_a)
    
    else:
        circuits.append({box_a, box_b})

    count += 1


print(box_a[0]*box_b[0])