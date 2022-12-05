import matplotlib.pyplot as plt
import numpy as np

waiting_times = [100., 101., 102., 103., 104., 105., 106., 107., 108., 109., 110., 92., 128.]
waiting_times2 = [200., 201., 202., 203., 204., 205., 206., 207., 208., 209., 210., 181., 258.]
min, Q1, Q2, Q3, max = np.quantile(waiting_times, [0, 0.25, 0.5, 0.75, 1])

print(min, Q1, Q2, Q3, max)

#per evidenziare la media
plt.boxplot([waiting_times, waiting_times2], showmeans=True)
plt.show()