import math

def function1(x):
    return math.sin(x) - 2 * x**2 + 1/2

def function2(x):
    return math.sqrt(1 - x**2) - math.exp(x) + 0.1

def function3(x):
    return x**6 - 5 * x**3 + 3 * x + 2

def function4(x):
    return math.log(3 * x / 2) + (5 / (1 + x**2))

def function5(x):
    return 3**x - 5 * x + 1

def dichotomy_method(a, b, epsilon, function):
    iteration = 0
    while abs(b - a) > epsilon:
        c = (a + b) / 2
        iteration += 1
        if function(c + epsilon) < function(c - epsilon):
            a = c
        else:
            b = c
        print("Итерация:", iteration)
        print("Текущее приближение:", c)
    return (a + b) / 2

# Список функций
functions = [function1, function2, function3, function4, function5]

# Интервалы для каждой функции
intervals = [
    lambda x: (-2, 2),
    lambda x: (-1, 0),
    lambda x: (-1, 1),
    lambda x: (0, 1),
    lambda x: (-1, 1)
]

# Вызов метода дихотомии для каждой функции
for i, func in enumerate(functions):
    print("Функция", i+1)
    interval = intervals[i](func)
    print("Интервал:", interval)
    a, b = interval
    epsilon = 1e-4
    extremum = dichotomy_method(a, b, epsilon, func)
    print("Экстремум функции:", extremum)
    print("Значение функции в экстремуме:", func(extremum))
    print()