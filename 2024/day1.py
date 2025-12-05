raw  = open('data.txt','r').read()
score = 0

##part1
# l1, l2 = [],[]
# for l in raw.split('\n'):
#     n1, n2 = l.split('   ')
#     l1.append(int(n1))
#     l2.append(int(n2))
#
# l1.sort()
# l2.sort()
# 
# for i in range(len(l1)):
#     score += abs(l1[i]-l2[i])


##part2
l1 = []
seen = {}
for l in raw.split("\n"):
    n1, n2 = map(int, l.split("   "))
    l1.append(n1)
    if n2 not in seen:
        seen[n2] = 0
    seen[n2] += 1


for n in l1:
    if n in seen:
        score += n*seen[n]

print(score)    