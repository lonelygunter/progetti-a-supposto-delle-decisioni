import pulp as p
from pulp import PULP_CBC_CMD

# apro il file in modalità lettura
f = open('branch-and-bound/toy76.txt', 'r')


# variabili
N = int(f.readline())
nodi = range(0, N)
costi = [[int(num) for num in line.split('\t')] for line in f]
problem = p.LpProblem("Traveller", p.const.LpMinimize)
STARTING_NODE = 0

x = p.LpVariable.dicts('x', ((i, j) for i in nodi for j in nodi), lowBound=0, upBound=1, cat=p.LpBinary)
u = p.LpVariable.dicts('u', nodi, lowBound=1, cat=p.LpInteger)


# funzione obiettivo
problem += p.lpSum(costi[i][j] * x[i, j] for i in nodi for j in nodi if i != j)


# vicoli
for i in nodi:
    if i != nodi[STARTING_NODE]:
        problem += u[i] >= 2
        problem += u[i] <= N

for i in nodi:
    problem += p.lpSum([x[i, j] for j in nodi if i != j]) == 1

for j in nodi:
    problem += p.lpSum([x[i, j] for i in nodi if i != j]) == 1

for i in nodi:
    for j in nodi:
        if i != j and (i != STARTING_NODE and j != STARTING_NODE):
            problem += u[i] - u[j] + 1 <= N * (1 - x[i, j])


# solver
problem.solve(PULP_CBC_CMD(msg=True))

for i in nodi:
    print("Punto {} ordine di visita: {}".format(i+1, u[i].varValue))