import numpy as np

u = np.array([[4, 5, 0.01], [2, 3, 4]])
v = np.array([[2, 2, 0.03], [1, 1, 1]])

total = (u**2 + v**2)**0.5
print(total)

condition = np.less(total, 0.1)
total_corr = np.where(condition, 0.1, total)
print(total_corr)
