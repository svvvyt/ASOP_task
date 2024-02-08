import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Функция Розенброка
def rosenbrock(x, y):
    return (1 - x)**2 + 100 * (y - x**2)**2

# Создание сетки точек для отображения функции
x_vals = np.linspace(-2, 2, 100)
y_vals = np.linspace(-1, 3, 100)
x_grid, y_grid = np.meshgrid(x_vals, y_vals)
z_grid = rosenbrock(x_grid, y_grid)

# Генерация 3D-графика
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x_grid, y_grid, z_grid, cmap='viridis', alpha=0.8)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z (Rosenbrock Function)')
ax.set_title('3D Plot of Rosenbrock Function')

# Отображение графика
plt.show()