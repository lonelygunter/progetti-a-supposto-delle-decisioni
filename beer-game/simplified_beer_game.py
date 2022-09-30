from beer_demand import get_demand
import matplotlib.pyplot as plt

#########################################################################################
# plot(series): plots a time series
# y: time series y_0, y_1, ... to be plotted
# name: name of the time series
def plot(y, name):
    plt.plot(y, 'ro')
    plt.ylabel(name)
    plt.show()


demand = []
for t in range(0, 20):
    demand.append(get_demand(t))

print(demand)
plot(demand, "Demand")