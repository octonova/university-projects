import numpy as np

def distance_to_line(x_hat, a, b):
    a_transpose = np.transpose(a)
    numerator = np.linalg.norm((x_hat - a * np.dot(a_transpose, (x_hat - b))))  # ||(𝑥̂ - 𝑎𝑡 - 𝑏) - 𝑎^𝑇(𝑥̂ - 𝑎𝑡 - 𝑏)||
    denominator = np.linalg.norm(a)  # ||𝑎||
    distance = numerator / denominator
    return distance

n = 3  # Размерность пространства
x_hat = np.array([1, 2, 3])  # Точка в ℝ𝑛
a = np.array([2, -1, 0])  # Вектор a
b = np.array([1, 1, 1])  # Вектор b

distance = distance_to_line(x_hat, a, b)
print(f"Расстояние от точки {x_hat} до прямой 𝑥 = {a}𝑡 + {b} равно {distance}.")
