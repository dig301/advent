raw = open("data.txt", 'r').read().split('\n')

pos = 50
score = 0
for instruction in raw:
    step = int(instruction[1:]) * (1 if instruction[0] == "R" else -1)
    direction = 1 if step > 0 else -1
    for _ in range(abs(step)):
        pos = (pos + direction) % 100
        if pos == 0:
            score += 1

print(score)
#bruteforce solution
