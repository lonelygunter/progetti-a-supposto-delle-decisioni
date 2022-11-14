import random as r
import matplotlib as plt

# dopo ogni iterazione perdiamo in media: 1/6 * 4 - 5/6 * 1 = -1/6
n = 6
win = 4
lose = 1
fattPerd = 1/n * win - 5/n * lose

partite = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

for i in range(0,len(partite)):
    print('partita: ', i+1)
    
    capMed=0
    for k in range(0, 1000):
        euro=1000
        for j in range(0, partite[i]):
            u1 = r.randrange(0, n)
            u2 = r.randrange(0, n)
            #print(u1, " | ", u2, " | ", euro)
            if (u1 == u2):
                euro += win
            else:
                euro -= lose
        capMed +=euro
    
    capMed /= 1000
    print("capitale medio: ", capMed)
    print("Fattore di perdita: ", fattPerd * partite[i], "\n")