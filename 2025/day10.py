import pulp
import itertools
import z3

lines = open("data.txt", 'r').read().splitlines()


lights = [l.split("]")[0][1:] for l in lines]

_joltages = [l.split("{")[1][:-1] for l in lines]
joltages = [list(map(int, j.split(','))) for j in _joltages]

buttons = []
for line_index, line in enumerate(lines):
    button_section = line.split("]")[1].split("{")[0].strip()
    button_defs = button_section.split()
    
    line_buttons = []
    num_counters = len(joltages[line_index])

    for btn in button_defs:
        indexes = [int(i) for i in btn.strip("()").split(",")]
        
        vector = [1 if i in indexes else 0 for i in range(num_counters)]
        line_buttons.append(vector)
    
    buttons.append(line_buttons)


score = 0
##part1
# for i in range(len(lights)):
#     N = len(lights[i])
#     final = [1 if v == "#" else 0 for v in lights[i]]

#     button_flips = buttons [i]
        
#     found_comb = False
#     for j in range(1, len(buttons)+1):
#         combs = itertools.combinations(button_flips, j)

#         if found_comb:
#             break

#         for c in combs:
#             xor_result = [0]*N
#             for mask in c:
#                 xor_result = [x ^ y for x, y in zip(xor_result, mask)]            
        
#             if xor_result == final:
#                 found_comb = True
#                 score += j
#                 break
# print(score)


##part2

#approach #1 -> solve matrix
# example: (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7} 

# A =  [[0,0,0,1]            
#       [0,1,0,1]                
#       [0,0,1,0]            
#       [0,0,1,1]
#       [1,0,1,0]            
#       [1,1,0,0]]    
# B = [3,5,4,7]
# (A^T)*X=B -> find x         
for i in range(len(joltages)):
    target = joltages[i]
    N = len(target)

    
    A_T = [list(x) for x in zip(*buttons[i])]

    num_buttons = len(A_T[0])
    num_counters = len(A_T)

    # https://z3prover.github.io/api/html/z3.z3.html
    # step1: define variables and optimizer
    # step2: define constraints for variables and optimizer
    # step3: check validity (required)
    # step4: model

    solver = z3.Optimize()
    X = [z3.Int(f"x{j}") for j in range(num_buttons)]

    for var in X:
        solver.add(var >= 0)
    
    for j in range(num_counters):
        solver.add(z3.Sum([A_T[j][c] * X[c] for c in range(num_buttons)]) == target[j])

    solver.minimize(z3.Sum(X))

    # print(solver.help)
    if solver.check() == z3.sat:
        model = solver.model()
        score += sum([model[var].as_long() for var in X])
print(score)
