raw = open("data.txt", 'r').read()

data = [line.split() for line in raw.split("\n")]


##part1
# transposed = [list(row) for row in zip(*data)]

# score = 0
# for r in transposed:
#     row_score = None
#     for v in r[:-1]:
#         val = int(v)
#         if row_score is None:
#             row_score = val
#             continue

#         if r[-1] == '*':
#             row_score *= val
#         elif r[-1] == '+':
#             row_score += val
#     score += row_score



##part2
transposed = [list(row) for row in zip(*raw.split("\n"))]
transposed += [' '* len(transposed[0])] # add padding for last line to be processed

score = 0
numbers = []
operation = None
for raw_col in transposed:
    col = "".join(raw_col).strip()
    if not col:
        if operation == '+':
            colscore = sum(numbers)
        elif operation == '*':
            colscore = 1
            for n in numbers:
                colscore *= n

        score += colscore
        operation = None
        numbers = []
        continue

    #get op and remove char from string
    for op in "*+":
        if op in col:
            operation = op
            col = col.replace(op,'')
            break

    numbers.append(int(col))
print(score)


