raw = open("data.txt", 'r').read()

score = 0
i = 0
N = len(raw)
raw += "###########################"


def get_number(idx, data):
    n = 0
    
    while n < 1000000 and data[idx].isdigit():
        n = 10 * n + int(data[idx])
        idx += 1
    if 1 <= n <= 999999:
        return n, idx
    return None, idx


##part1
# while i<N:
#     if "".join(raw[i:i+4]) == "mul(":
#         i+=4
#         x,i = get_number(i, raw)
#         if raw[i] == ',':
#             i+=1
#             y,i = get_number(i, raw)
#             if raw[i] == ')':
#                 if x is not None and y is not None:
#                     score += x*y
#     i+=1


##part2
enable = True
while i<N:
    if "".join(raw[i:i+4]) == "do()":
        enable = True

    if "".join(raw[i:i+7]) == "don't()":
        enable = False

    if "".join(raw[i:i+4]) == "mul(":
        i+=4
        x,i = get_number(i, raw)
        if raw[i] == ',':
            i+=1
            y,i = get_number(i, raw)
            if raw[i] == ')':
                if x is not None and y is not None and enable:
                    score += x*y
    i+=1

print(score)