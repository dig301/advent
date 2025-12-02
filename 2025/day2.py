raw = open("data.txt",'r').read().split(',')

##part1
# score = 0
# for r in raw:
#     start, end = list(map(int, r.split('-')))
#     for n in range(start, end+1):
#         n_sz = len(str(n))
#         if n_sz%2==0:
#             if str(n)[n_sz//2:] == str(n)[:n_sz//2]:
#                 score += n
# print(score)


##part2
score = 0
for r in raw:
    start, end = list(map(int, r.split('-')))
    toscore = set()
    for n in range(start, end+1):
        token_sz = 1
        n_sz = len(str(n))
        while token_sz <= n_sz // 2:
            if n_sz % token_sz == 0:
                token = str(n)[:token_sz]
                if token * (n_sz // token_sz) == str(n):
                    score += n
                    break

            token_sz += 1

print(score)