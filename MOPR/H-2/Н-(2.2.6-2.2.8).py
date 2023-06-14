import numpy as np
from scipy.optimize import differential_evolution

# Функция 1: 𝑓(𝑥1, 𝑥2) = 𝑥1**2 + 𝑥2**2 − 2*𝑥1 − 4*𝑥2 + 5
def function1(x):
    return x[0]**2 + x[1]**2 - 2*x[0] - 4*x[1] + 5

# Градиент функции 1
def gradient1(x):
    return np.array([2*x[0] - 2, 2*x[1] - 4])

# Функция 2: 𝑓(𝑥1, 𝑥2) = 2*𝑥1**2 − 2*𝑥1*𝑥2 + 𝑥2**2 + 2*𝑥1 − 2*𝑥2
def function2(x):
    return 2*x[0]**2 - 2*x[0]*x[1] + x[1]**2 + 2*x[0] - 2*x[1]

# Градиент функции 2
def gradient2(x):
    return np.array([4*x[0] - 2*x[1] + 2, -2*x[0] + 2*x[1] - 2])

# Функция 3: 𝑓(𝑥1, 𝑥2, 𝑥3) = 𝑥1**2 + 2*𝑥2**2 + 𝑥3**2 − 2*𝑥1*𝑥2 − 𝑥1 + 2*𝑥3
def function3(x):
    return x[0]**2 + 2*x[1]**2 + x[2]**2 - 2*x[0]*x[1] - x[0] + 2*x[2]

# Градиент функции 3
def gradient3(x):
    return np.array([2*x[0] - 2*x[1] - 1, -2*x[0] + 4*x[1], 2*x[2] + 2])

# Функция 4: 𝑓(𝑥1, 𝑥2, 𝑥3) = 𝑥1**2 + 𝑥2**2 + 𝑥3**2 − 𝑥1*𝑥2 + 𝑥1 − 2*𝑥3
def function4(x):
    return x[0]**2 + x[1]**2 + x[2]**2 - x[0]*x[1] + x[0] - 2*x[2]

# Градиент функции 4
def gradient4(x):
    return np.array([2*x[0] - x[1] + 1, -x[0] + 2*x[1], 2*x[2] - 2])

# Функция 6: 𝑓(𝑥1, 𝑥2) = 𝑥1**2 + 𝑥2**2 - 0.2*𝑥1*𝑥2 − 2.2*𝑥1 + 2.2*𝑥2 + 2.2
def function6(x):
    return x[0]**2 + x[1]**2 + x[2]**2 - x[0]*x[1] + x[0] - 2*x[2]

# Градиент функции 6
def gradient6(x):
    return np.array([2*x[0] - 0.2*x[1] - 2.2, 2*x[1] - 0.2*x[0] + 2.2, 2*x[2] - 2])

# Функция 7: 𝑓(𝑥1, 𝑥2) = 5𝑥1**2 + 4.075𝑥2**2 - 9*𝑥1*𝑥2 + 𝑥1 + 2
def function7(x):
    x1, x2 = x
    return 5*x1**2 + 4.075*x2**2 - 9*x1*x2 + x1 + 2

# Градиент функции 7
def gradient7(x):
    x1, x2 = x
    return np.array([10*x1 - 9*x2 + 1, 8.15*x2 - 9*x1])

# Метод скорейшего спуска
def steepest_descent(func, grad, initial_point, learning_rate=0.1, epsilon=1e-6, max_iterations=1000):
    x = initial_point
    iteration = 0

    while iteration < max_iterations:
        gradient = grad(x)

        if np.linalg.norm(gradient) < epsilon:
            break
        x = x - learning_rate * gradient
        iteration += 1

    return x, func(x)

# Поиск минимума для функции 1
initial_point1 = np.array([0.0, 0.0])
min_point1, min_value1 = steepest_descent(function1, gradient1, initial_point1)
print("Минимум функции 1:")
print("Координаты: {:.3f}, {:.3f}".format(*min_point1))
print("Значение: {:.3f}".format(min_value1))

# Поиск минимума для функции 2
initial_point2 = np.array([0.0, 0.0])
min_point2, min_value2 = steepest_descent(function2, gradient2, initial_point2)
print("Минимум функции 2:")
print("Координаты: {:.3f}, {:.3f}".format(*min_point2))
print("Значение: {:.3f}".format(min_value2))

# Поиск минимума для функции 3
initial_point3 = np.array([0.0, 0.0, 0.0])
min_point3, min_value3 = steepest_descent(function3, gradient3, initial_point3)
print("Минимум функции 3:")
print("Координаты: {:.3f}, {:.3f}, {:.3f}".format(*min_point3))
print("Значение: {:.3f}".format(min_value3))

# Поиск минимума для функции 4
initial_point4 = np.array([0.0, 0.0, 0.0])
min_point4, min_value4 = steepest_descent(function4, gradient4, initial_point4)
print("Минимум функции 4:")
print("Координаты: {:.3f}, {:.3f}, {:.3f}".format(*min_point4))
print("Значение: {:.3f}".format(min_value4))

# Поиск минимума для функции 6
initial_point6 = np.array([0.0, 0.0, 0.0])
min_point6, min_value6 = steepest_descent(function6, gradient6, initial_point6)
print("Минимум функции 6:")
print("Координаты: {:.3f}, {:.3f}, {:.3f}".format(*min_point6))
print("Значение: {:.3f}".format(min_value6))

# Поиск минимума для функции 7
initial_point7 = np.array([0.0, 0.0])
min_point7, min_value7 = steepest_descent(function7, gradient7, initial_point7)
print("Минимум функции 7:")
print("Координаты: {:.3f}, {:.3f}".format(*min_point7))
print("Значение: {:.3f}".format(min_value7))

# Функция 8: 𝑓(𝑋) = (𝑥1 + 10*𝑥2)**2 + 5*(𝑥3 − 𝑥4 + 2𝑘)**2 + (𝑥2 − 2𝑥3)**4 +100(𝑥1 − 𝑥4 + 11𝑘)**4
def function8(X, k):
    x1, x2, x3, x4 = X
    return (x1 + 10*x2)**2 + 5*(x3 - x4 + 2*k)**2 + (x2 - 2*x3)**4 + 100*(x1 - x4 + 11*k)**4

# Ограничения для переменных 𝑋
bounds = [(-10, 10)] * 4

# Метод дифференциальной эволюции
def differential_evolution_minimization(func, bounds, k, epsilon):
    res = differential_evolution(func, bounds, args=(k,), tol=epsilon)
    return res.x, res.fun, res.nit

# Заданный параметр k
k = 2

# Точность для различных значений n
epsilon_values = [1e-2, 1e-3, 1e-4, 1e-5, 1e-10, 1e-12, 1e-15]

# Начальные значения
initial_point = np.array([0.0, 0.0, 0.0, 0.0])

# Функция форматирования значения
def format_value(value):
    integer_part = int(value)
    fractional_part = value - integer_part
    if fractional_part == 0:
        return f"{integer_part}.000"
    else:
        return f"{integer_part}.{str(fractional_part)[:3]}"

# Вычисление и вывод минимума функции
print("Решение функции 8:")
for epsilon in epsilon_values:
    min_point, min_value, num_iterations = differential_evolution_minimization(function8, bounds, k, epsilon)
    formatted_point = [format_value(coord) for coord in min_point]
    print(f"Точность: {epsilon}")
    print(f"Минимум функции: f({', '.join(formatted_point)}) = {format_value(min_value)}")
    print(f"Число итераций: {num_iterations}")
    print("----------------------------------")


