import pulp as p
from pulp import PULP_CBC_CMD

f = open('branch-and-bound/toy.txt', 'r')
N = int(f.readline())

nodi = range(0, N)

problem = p.LpProblem("Traveller", p.const.LpMinimize)
costi = [[int(num) for num in line.split('\t')] for line in f]

STARTING_NODE = 0


#Vincoli
x = p.LpVariable.dicts('x', ((i, j) for i in nodi for j in nodi), lowBound=0, upBound=1, cat=p.LpBinary)
u = p.LpVariable.dicts('u', nodi, lowBound=1, cat=p.LpInteger)

# Funzione obiettivo
problem += p.lpSum(costi[i][j] * x[i, j] for i in nodi for j in nodi if i != j)

for i in nodi:
    if i != nodi[STARTING_NODE]:
        problem += u[i] >= 2
        problem += u[i] <= N
        # for j in nodi:
        #     if j != nodi[STARTING_NODE]:
        #         problem += u[i] - u[j] + 1 <= N * (1-x[i, j])

for i in nodi:
    problem += p.lpSum(x[i, j] for j in nodi) == 1
    problem += p.lpSum(x[j, i] for j in nodi) == 1

for i in nodi:
    for j in nodi:
        if i != j and (i != STARTING_NODE and j != STARTING_NODE):
            problem += u[i] - u[j] <= N * (1 - x[i, j]) - 1

problem.solve(PULP_CBC_CMD(msg=True))

for i in nodi:
    print("Punto {} ordine di visita: {}".format(i, u[i].varValue))