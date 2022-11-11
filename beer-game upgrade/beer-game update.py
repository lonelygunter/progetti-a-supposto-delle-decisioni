from pulp import *
import beer_demand

# data
T = 20  # number of time periods of the planning horizon
h = 1 # unit inventory cost
b = 1 # backlog unit cost
f = 100 # fixed production cost
c = 18  # unit variable production cost
d = []
for t in range(T):
    d.append(beer_demand.get_demand(t))     # demand over the planning horizon
Q = 1000 # warehouse capacity
I_0 = 540 # initial inventory level
I_f = 0 # inventory level at the end of the planning horizon
B_f = 0 # backlog level at the end of the planning horizon
L = 2 # lead time

# define planning horizon
period = range(T)

# define problem
model = LpProblem("single_product_lot_sizing", LpMinimize)

# define decision variables
y = LpVariable.dicts('order_issued', period, lowBound=0, upBound=1, cat='Integer')
x = LpVariable.dicts('order_amount', period, lowBound = 0, cat='Continuous')
I = LpVariable.dicts('inventory_level', period, lowBound = 0, cat='Continuous')
B = LpVariable.dicts('backlog_level', period, lowBound = 0, cat='Continuous')

# define objective function
model += lpSum([f*y[i] + h*I[i] + b*B[i] + c*x[i] for i in period])

# setup iniziale
if d[0] < I_0:
    I[0] = I_0 - d[0]
    B[0] = b
else:
    I[0] = 0
    B[0] = d[0] - I_0


# constraints
for t in period[1:L]:
    model += I[t - 1] - B[t - 1] - d[t] == I[t] - B[t]

for t in period[L:]:
    model += I[t - 1] - B[t - 1] +x[t-L] - d[t] == I[t] - B[t]



model += I[T-1] == I_f
model += B[T-1] == B_f

for t in period:
    model += I[t]  <= Q

for t in period:
    M = 0
    for tt in period[t:]:
        M += d[tt]
    model += x[t] <= M * y[t]

# solve the problem
model.solve(PULP_CBC_CMD(msg=True))

# print results
print("Optimal solution:")
print("* Cost: {}\n".format(value(model.objective)))
for i in period:
    if y[i].varValue:
        print("* y[{}] = {}".format(i, y[i].varValue))
    if x[i].varValue:
        print("* x[{}] = {}".format(i, x[i].varValue))
