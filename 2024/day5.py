raw = open("data.txt", 'r').read()


rules, tests = raw.split('\n\n')
score = 0

def is_ok(aa, rules):
    for rule in rules.split("\n"):
        n1, n2 = rule.split("|")
        if n1 not in aa or n2 not in aa:
            continue
        if aa[n1] < aa[n2]:
            continue
        
        return False, rule
    return True, rule

##part1
# for test in tests.split("\n"):
#     aa = {}
#     for i, val in enumerate(test.split(",")):
#         aa[val] = i

#     if is_ok(aa, rules)[0]:
#         _l = [int(n) for n in test.split(",")]
#         score += _l[len(_l)//2]



##part2
for test in tests.split("\n"):
    aa = {}
    for i, val in enumerate(test.split(",")):
        aa[val] = i


    status, offending_rule = is_ok(aa, rules)
    if status:
        continue

    while status == False:
        n1, n2 = offending_rule.split("|")
        aa[n1], aa[n2] = aa[n2], aa[n1]
        status, offending_rule = is_ok(aa, rules)
        # find which rules violates 
        # swap n1 <-> n2

    for k,v in aa.items():
        if v == len(aa)//2:
            score += int(k)
        

print(score)




