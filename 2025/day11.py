import functools
lines = [l.strip() for l in open("data.txt", 'r').readlines()]

paths = dict()
for l in lines:
    k,v = l.split(":")
    paths[k] = [x for x in v.split()]


##part1
# def count_paths(node):
#     if node == "out":
#         return 1
    
#     total = 0
#     for nxt in paths.get(node, []):       
#         total += count_paths(nxt)

#     return total
# score = count_paths("you")


##part2
@functools.lru_cache
def get_paths(node, fft_in_path, dac_in_path):
    if node == "out":
        if fft_in_path and dac_in_path:
            return 1
        return 0
    
    total = 0
    for nxt in paths.get(node, []):     
        fft_in_path = fft_in_path or nxt == "fft"
        dac_in_path = dac_in_path or nxt == "dac"
        total += get_paths(nxt, fft_in_path, dac_in_path)

    return total
score = get_paths("svr", False, False)


print(score)
