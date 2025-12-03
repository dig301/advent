lines = open("data.txt",'r').read().split('\n')

def num_from_list(lst):
    out = 0
    exp = len(lst)-1
    for n in lst:
        out += n * 10**exp
        exp -= 1
    return out

def get_num(mask, line):
    num_l = [line[m] for m in mask]
    return num_from_list(num_l)

# N = 2 ## part1
N = 12  ## part2
score = 0
for _l in lines:
    line = [int(n) for n in _l]
    mask = [n for n in range(N)]

    num = get_num(mask, line)
    max_num = num

    for i in range(N, len(line)):
        tmp_new_mask = mask + [i]
        
        for j in range(len(tmp_new_mask)):
            testmask = tmp_new_mask[:j] + tmp_new_mask[j+1:]
            testnum = get_num(testmask, line)

            if testnum > max_num:
                max_num = testnum
                mask = testmask

    score += max_num

print(score)



        