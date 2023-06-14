import numpy as np
from scipy.optimize import linprog

# Задача 1
c1 = np.array([1, 1, 1, 1])
A_eq1 = np.array([[4, 2, 5, -1],
                 [5, 3, 6, -2],
                 [3, 2, 4, -1]])
b_eq1 = np.array([5, 5, 4])

# Решение задачи 1
res1 = linprog(-c1, A_eq=A_eq1, b_eq=b_eq1, bounds=(0, None), method='simplex')

# Вывод результатов задачи 1
print("Задача 1:")
print("Оптимальный план:")
for i, val in enumerate(res1.x):
    print(f"x{i+1} = {val:.3f}")
print(f"F(X) = {-res1.fun:.3f}")

# Задача 2
c2 = np.array([2, -1, 1, 0, -1])
A_eq2 = np.array([[-2, 0, 1, 0, 1],
                  [0, -2, 0, 1, 1]])
b_eq2 = np.array([-3, 2])
A_ub2 = np.array([[1, 3, -1, 0, 0],
                  [-1, -1, 0, 0, 0]])
b_ub2 = np.array([-5, 3])

# Решение задачи 2
res2 = linprog(-c2, A_eq=A_eq2, b_eq=b_eq2, A_ub=A_ub2, b_ub=b_ub2, bounds=(0, None), method='simplex')

# Вывод результатов задачи 2
print("\nЗадача 2:")
print("Оптимальный план:")
for i, val in enumerate(res2.x):
    print(f"x{i+1} = {val:.3f}")
print(f"F(X) = {-res2.fun:.3f}")
