import pulp as pu
import numpy as np
import matplotlib.pyplot as plt

# Data
Tasks = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

d = {'A': 10, 'B': 15, 'C': 20, 'D': 15, 'E': 5, 'F': 10, 'G': 5, 'H': 20} # durate nominali

dm = 8 # durata minima

w = 1 # riduzione della durata dei task

B = 30 # budget

p = {'A': {'A': 0, 'B': 1, 'C': 1, 'D': 1, 'E': 0, 'F': 0, 'G': 0, 'H': 0},
    'B': {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 1, 'H': 0},
    'C': {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 1, 'F': 0, 'G': 0, 'H': 0},
    'D': {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 1},
    'E': {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 1, 'G': 1, 'H': 0},
    'F': {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 1},
    'G': {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 1},
    'H': {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0}} # Precedences

risultati = []

for i in range(0, B):
    #definisco il modello
    model = pu.LpProblem('ProjectSchedulingModel', pu.const.LpMinimize)

    s = pu.LpVariable.dict('s', Tasks, 0, cat=pu.const.LpContinuous) # start times
    T = pu.LpVariable('T', 0,  cat=pu.const.LpContinuous)
    x = pu.LpVariable.dict('x', Tasks, 0, cat=pu.const.LpContinuous) # B assegnato


    #define objective function
    model += T

    #define constraints
    for i in Tasks:
        model += s[i] + d[i] - (w * x[i]) <= T
        model += d[i] - (w * x[i]) >= dm
        for j in Tasks:
            if p[i][j] == 1:
                model += s[i] + d[i] - (w * x[i]) <= s[j]

    model += pu.lpSum(x) <= B

    #solver = pu.getSolver()
    model.solve()

    # decrement the budget
    B -= 1
    
    # insert new append 
    risultati.append([T.varValue, B])


data = np.array(risultati)
x, y = data.T
plt.scatter(x, y)
plt.show()