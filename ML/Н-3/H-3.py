import pandas as pd
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

# Загрузка данных из CSV-файлов
train_data = pd.read_csv('preprocessed_train_data.csv', sep=';')
test_data = pd.read_csv('preprocessed_test_data.csv', sep=';')

# Разделение данных на признаки (X) и целевую переменную (y)
X_train = train_data.drop(['Id', 'SalePrice'], axis=1)
y_train = train_data['SalePrice']
X_test = test_data.drop('Id', axis=1)

# Масштабирование признаков
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Создание экземпляра SimpleImputer с заполнением средними значениями
imputer = SimpleImputer(strategy='mean')

# Заполнение пропущенных значений в тестовых данных
X_test_imputed = imputer.fit_transform(X_test_scaled)

# Создание модели SVR и ее обучение
svr = SVR()
svr.fit(X_train_scaled, y_train)

# Прогнозирование на тестовом наборе
y_pred = svr.predict(X_test_imputed)

# Создание таблицы с прогнозами для вывода в терминал
output_table = pd.DataFrame({'Id': test_data['Id'], 'SalePrice': y_pred})
print(output_table)
