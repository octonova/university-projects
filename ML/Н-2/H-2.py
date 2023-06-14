import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split

# Создаем искусственные данные полумесяцев
X, y = make_moons(n_samples=500, noise=0.1, random_state=42)

# Разделяем данные на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Создаем экземпляр SVC и обучаем модель
model = SVC(kernel='rbf', C=1.0, gamma='scale', probability=True, random_state=42)
model.fit(X_train, y_train)

# Вычисляем точность модели на тестовой выборке
accuracy = model.score(X_test, y_test)

# Создаем сетку точек для визуализации границы принятия решений
xx, yy = np.meshgrid(np.linspace(-2, 3, num=100), np.linspace(-1, 2, num=100))
Z_proba = model.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]
Z_proba = Z_proba.reshape(xx.shape)

# Визуализируем границу принятия решений и данные с градиентным отображением на линии соприкосновения
plt.figure(figsize=(8, 6), dpi=80)
plt.contourf(xx, yy, Z_proba, cmap=plt.cm.RdBu, alpha=0.4)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.RdBu)
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.xlabel('X', fontsize=10)
plt.ylabel('Y', fontsize=10)
plt.title(f'Точность модели на тестовой выборке: {accuracy}')
plt.show()
