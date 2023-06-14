from pulp import *

pulp.LpSolverDefault.msg = 0

# Определение переменных
x = LpVariable.dicts("x", [(i, j) for i in range(1, 5) for j in range(1, 5)], lowBound=0)

# Создание модели и определение целевой функции для задачи
model = LpProblem("Transportation Problem", LpMinimize)
model += lpSum([x[(i, j)] * [2, 3, 4, 1, 3, 4, 2, 5, 1, 7, 5, 7, 5, 2, 8, 2][4 * (i-1) + (j-1)] for i in range(1, 5) for j in range(1, 5)])

# Добавление ограничений для задачи
supply = [7, 11, 8, 2]
demand = [7, 8, 5, 6]
for i in range(1, 5):
    model += lpSum([x[(i, j)] for j in range(1, 5)]) <= supply[i-1]
for j in range(1, 5):
    model += lpSum([x[(i, j)] for i in range(1, 5)]) >= demand[j-1]

# Решение задачи
model.solve()

# Вывод результатов
print("Решение транспортной задачи №2:")
print("Оптимальный план:")
for i in range(1, 5):
    for j in range(1, 5):
        print(f"x{i}{j} = {value(x[(i, j)])}")
print(f"F(X) = {value(model.objective)}")
