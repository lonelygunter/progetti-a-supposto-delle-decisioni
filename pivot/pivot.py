# procedure per creare la funzione makePivot(r,s)

pivot = a[r,s]

for j in range(0, n):
    a[r,j] = a[r,j]/pivot

    for i in range(0, m):
        if i != r:
            factor = a[i, s]

            for j in range(0, n):
                a[i, j] = a[i, j] - factor * a[r, j]

