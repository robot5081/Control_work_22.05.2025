# Уровень B
# №1
import pandas as pd
def main():
    # Загрузка Excel файла
    file_path = 'Book1.xlsx'  # Укажите путь к вашему Excel файлу
    df = pd.read_excel(file_path)
    # Запрос пользователя
    query = input("Введите значение для поиска: ")
    # Поиск строки с нужным значением
    result = df[df.apply(lambda row: row.astype(str).str.contains(query).any(), axis=1)]
    # Вывод результата
    if not result.empty:
        print("Найденные строки:")
        print(result)
    else:
        print("Строки не найдены.")
if __name__ == "__main__":
    main()



# №2
import pandas as pd
import matplotlib.pyplot as plt

# Шаг 1: Считываем данные из Excel
file_path = 'Book1.xlsx'  # Путь к файлу Excel
df = pd.read_excel(file_path)

# Проверяем структуру данных
print(df.head())  # Вывод первых строк для проверки

# Шаг 2: Построение графика
plt.figure(figsize=(8, 6))  # Размер окна графика

# Используем данные из DataFrame
plt.plot(df['x'], df['y'], marker='o', label='Зависимость y от x')

# Настройка графика
plt.title('График из Excel')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.legend()
plt.grid(True)  # Включить сетку

# Шаг 3: Отображаем график
plt.show()



# №3
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LightSource

# Создаем координаты X, Y
X = np.linspace(-5, 5, 10)
Y = np.linspace(-5, 5, 10)
X_grid, Y_grid = np.meshgrid(X, Y)

# Функция рельефа (горы и холмы)
Z_grid = np.sin(np.sqrt(X_grid**2 + Y_grid**2)) * 2 + np.cos(Y_grid) * 1.5

# Добавляем источник света
ls = LightSource(azdeg=315, altdeg=45)

# Используем plt.cm.terrain вместо 'terrain'
shaded_Z = ls.shade(Z_grid, cmap=plt.cm.terrain, vert_exag=0.2, blend_mode='soft')

# Создаем 3D-график
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Отображаем рельеф с тенью
ax.plot_surface(X_grid, Y_grid, Z_grid, facecolors=shaded_Z, rstride=1, cstride=1)

# Настройки осей
ax.set_xlabel("X координата")
ax.set_ylabel("Y координата")
ax.set_zlabel("Высота (Z)")

plt.show()