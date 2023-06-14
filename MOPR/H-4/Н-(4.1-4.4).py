import numpy as np


def simplex_method(c, A, b, x_start):
    m, n = A.shape

    # Добавление искусственных переменных
    c = np.concatenate((c, np.zeros(m)))
    A = np.hstack((A, np.eye(m)))

    # Изменение целевой функции для искусственных переменных
    c[:n] = np.zeros(n)

    # Изменение базиса для искусственных переменных
    basis = np.arange(n, n + m)

    # Изменение угловой точки
    x = np.concatenate((x_start, b))

    while True:
        # Вычисление плановой таблицы
        B = A[:, basis]
        c_B = c[basis]
        c_N = c[:n]
        x_B = x[basis]
        x_N = x[:n]

        B_inv = np.linalg.inv(B)
        c_B_B_inv = c_B @ B_inv

        # Вычисление оценок свободных переменных
        delta = c_N - c_B_B_inv @ A[:, :n]
        delta_B = np.zeros(m)

        # Проверка оптимальности
        if np.all(delta >= 0):
            break

        # Нахождение входящей переменной
        entering_var = np.argmax(delta)

        # Вычисление отношения RHS к коэффициентам в столбце входящей переменной
        ratios = x_B / A[:, entering_var]

        # Проверка на неограниченность
        if np.all(ratios <= 0):
            raise Exception("Задача неограничена")

        # Нахождение исходящей переменной
        leaving_var = np.argmin(ratios[ratios > 0])

        # Пересчет угловой точки и базиса
        x[entering_var] = ratios[leaving_var]
        x[basis[leaving_var]] = 0
        x -= x[entering_var] * A[:, entering_var]
        x[entering_var] = 0
        x[basis[leaving_var]] = 1

        basis[leaving_var] = entering_var

    return x[:n]


# Задача 1
c1 = np.array([-2, -1, -1, -7, 2])
A1 = np.array([[1, 1, -1, 1, 0],
               [2, 1, 1, 0, -1],
               [1, 2, 1, -7, 1]])
b1 = np.array([1, 7, 6])
x_start1 = np.array([2, 1, 2, 0, 0])

solution1 = simplex_method(c1, A1, b1, x_start1)
optimal_plan1 = solution1[:5]
optimal_f_value1 = np.dot(c1[:5], optimal_plan1)

print("Задача 1:")
print("Оптимальный план:")
print("x1 =", optimal_plan1[0])
print("x2 =", optimal_plan1[1])
print("x3 =", optimal_plan1[2])
print("x4 =", optimal_plan1[3])
print("x5 =", optimal_plan1[4])
print("F(X) =", optimal_f_value1)

# Задача 2
c2 = np.array([5, -4, 1, 3, 5])
A2 = np.array([[3, -1, 0, 2, 1],
               [2, -3, 1, 2, 1],
               [3, -1, 1, 3, 2]])
b2 = np.array([5, 6, 9])
x_start2 = np.array([0, 0, 1, 2, 1])

solution2 = simplex_method(c2, A2, b2, x_start2)
optimal_plan2 = solution2[:5]
optimal_f_value2 = np.dot(c2[:5], optimal_plan2)

print("\nЗадача 2:")
print("Оптимальный план:")
print("x1 =", optimal_plan2[0])
print("x2 =", optimal_plan2[1])
print("x3 =", optimal_plan2[2])
print("x4 =", optimal_plan2[3])
print("x5 =", optimal_plan2[4])
print("F(X) =", optimal_f_value2)

# Задача 3
c3 = np.array([1, 2, 2, 1, 6])
A3 = np.array([[1, 3, 3, 1, 9],
               [1, 5, 0, 8, 13],
               [0, 0, 1, 0, 1]])
b3 = np.array([18, 13, 3])
x_start3 = np.array([0, 1, 2, 0, 1])

solution3 = simplex_method(c3, A3, b3, x_start3)
optimal_plan3 = solution3[:5]
optimal_f_value3 = np.dot(c3[:5], optimal_plan3)

print("\nЗадача 3:")
print("Оптимальный план:")
print("x1 =", optimal_plan3[0])
print("x2 =", optimal_plan3[1])
print("x3 =", optimal_plan3[2])
print("x4 =", optimal_plan3[3])
print("x5 =", optimal_plan3[4])
print("F(X) =", optimal_f_value3)

# Задача 4
c4 = np.array([2, 1, 3, 1])
A4 = np.array([[1, 2, 5, -1],
               [1, -1, -1, 2]])
b4 = np.array([4, 1])
x_start4 = np.array([0, 0, 1, 1])

solution4 = simplex_method(c4, A4, b4, x_start4)
optimal_plan4 = solution4[:4]
optimal_f_value4 = np.dot(c4[:4], optimal_plan4)

print("\nЗадача 4:")
print("Оптимальный план:")
print("x1 =", optimal_plan4[0])
print("x2 =", optimal_plan4[1])
print("x3 =", optimal_plan4[2])
print("x4 =", optimal_plan4[3])
print("F(X) =", optimal_f_value4)
