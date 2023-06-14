from pulp import *

pulp.LpSolverDefault.msg = 0

# Определение переменных
x = LpVariable.dicts("x", [(i, j) for i in range(1, 5) for j in range(1, 5)], lowBound=0)

# Создание модели и определение целевой функции для задачи 1
model1 = LpProblem("Transportation Problem 1", LpMinimize)
model1 += lpSum([x[(i, j)] * [1, 3, 10, 6, 7, 2, 5, 8, 5, 2, 2, 9, 2, 1, 3, 4][4 * (i-1) + (j-1)] for i in range(1, 5) for j in range(1, 5)])

# Добавление ограничений для задачи 1
for i in range(1, 5):
    model1 += lpSum([x[(i, j)] for j in range(1, 5)]) <= [6, 14, 18, 11][i-1]
for j in range(1, 5):
    model1 += lpSum([x[(i, j)] for i in range(1, 5)]) >= [6, 14, 18, 11][j-1]

# Решение задачи 1
model1.solve()

# Вывод результатов задачи 1
print("Решение транспортной задачи №1:")
print("Оптимальный план:")
for i in range(1, 5):
    for j in range(1, 5):
        print(f"x{i}{j} = {value(x[(i, j)])}")
print(f"F(X) = {value(model1.objective)}")

