from random import seed, randrange

#########################################################################################
# WARNING: whan playing the wine game, do NOT look at the internal structure of this file
#########################################################################################

#########################################################################################
# get_demand(t): randomly generates the beer weekly demand (in pallets)
# t: week number (t=0, 1, ...)
def get_demand(t):
    if t==0:
        seed (1001001)
    if t < 10:
        T = 30+1*t
    else:
        T = 30+0.5*t
    if t%4 == 0:
        S = 1
    elif t%4 == 1:
        S = 0.97
    elif t%4 == 2:
        S = 0.92
    else:
        S = 0.89
    return randrange(round(T*S), round(T*S*1.1)+1, 1)

