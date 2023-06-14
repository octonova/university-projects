import numpy as np
import matplotlib.pyplot as plt
import json

# Чтение списка наборов точек из файла
with open('Наборы данных.json') as file:
    datasets = json.load(file)

# Создание сетки графиков
num_datasets = len(datasets)
fig, axs = plt.subplots(num_datasets, 1, figsize=(8, 4 * num_datasets))

# Проход по наборам точек и выполнение решения линейной регрессии
for i, dataset in enumerate(datasets):
    x = np.array(dataset['x'])
    y = np.array(dataset['y'])

    # Оценка коэффициентов регрессии
    coef = np.polyfit(x, y, 1)

    # Создание графика и отрисовка точек
    axs[i].scatter(x, y, color='green', label='Значения')

    # Отрисовка разделяющей линии
    x_line = np.linspace(np.min(x), np.max(x), 100)
    y_line = np.polyval(coef, x_line)
    axs[i].plot(x_line, y_line, color='red', label='Линия регрессии')

    axs[i].set_xlabel('x')
    axs[i].set_ylabel('y')
    axs[i].legend()
    axs[i].set_title(f"Набор значений {i+1}")

    # Вывод коэффициентов регрессии
    print(f"Результаты для набора данных {i+1}:")
    print(f"Наклон = {coef[1]}")
    print(f"Сдвиг = {coef[0]}")
    print()

# Отображение всех графиков
plt.tight_layout()
plt.show()
