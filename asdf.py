import random as r
from matplotlib import pyplot as plt

DICE_FACES = 6 # facce del dado
WIN_VALUE = 4 # premio in caso  di vittoria
LOSE_VALUE = 1 # perdita in caso di sconfitta
STARTING_BUDGET = 1000 # budget di partenza
RIPETIZIONI = 1000 # numero di ripetizioni dell'esperimento
LISTA_TIRI_PER_PARTITA = [200, 400, 1000] # lista che raccoglie il numero di tiri che vogliamo partita
listaPlots = [] #lista di tutti e 3 i plot

for nGiocate in LISTA_TIRI_PER_PARTITA:
    listaBilanciFinali = [] # lista che raccoglie i bilanci finali di ogni ripetizione
    listaRipetizioni = [] # lista che raccoglie tutti gli esperimenti di un plot
    for ripetizioni in range(RIPETIZIONI):
        listaBudget = [] # lista che raccoglie l'andamento del budget di un singolo esperimento
        ACTUAL_BUDGET = STARTING_BUDGET # riporto il budget al valore iniziale ad ogni partita
        for i in range(nGiocate):
            dice1 = r.randint(1, DICE_FACES)
            dice2 = r.randint(1, DICE_FACES)
            if dice1 == dice2:
                ACTUAL_BUDGET = ACTUAL_BUDGET + WIN_VALUE
            else:
                ACTUAL_BUDGET = ACTUAL_BUDGET - LOSE_VALUE
            listaBudget.append(ACTUAL_BUDGET)
        listaRipetizioni.append(listaBudget)
        listaBilanciFinali.append(ACTUAL_BUDGET)
    listaPlots.append(listaRipetizioni)
    print("------------------------------")
    print("Partite totali:      {}".format(RIPETIZIONI))
    print("Tiri per partita:    {}".format(nGiocate))
    print("Budget finale medio: {:.3f}".format(sum(listaBilanciFinali)/len(listaBilanciFinali)))

print("------------------------------")
print("Fattore di perdita:  {}*{:.2f} - {}*{:.2f} = {:.2f}".format(WIN_VALUE, 1/DICE_FACES, LOSE_VALUE, 
                                                                   (DICE_FACES-1)/DICE_FACES, WIN_VALUE*1/DICE_FACES -
                                                                   LOSE_VALUE*(DICE_FACES-1)/DICE_FACES))

plotNumero = 0
plt.figure(figsize=(15, 5))
for i in LISTA_TIRI_PER_PARTITA:
    ax = plt.subplot(1, len(LISTA_TIRI_PER_PARTITA), plotNumero+1)
    plt.title('Andamento del Budget su {} giocate'.format(i))
    plt.xlabel("Numero Giocate")
    if plotNumero == 0:
        plt.ylabel("Livello di Budget")
    for ripetizione in listaPlots[plotNumero]:
        plt.plot(ripetizione)
    plotNumero = plotNumero + 1
plt.show()