import numpy as np
import matplotlib.pyplot as plt

# Функция для визуализации (примерная функция ямы)
def terrain_function(x, y):
    return x**2 + y**2

# Функция покоординатного спуска
def coordinate_descent(start_point, func, step_size=0.09, max_iter=1000):
    path = [start_point]
    current_point = start_point

    for _ in range(max_iter):
        grad = np.array([func(*current_point)])

        if grad.size != 1:
            raise ValueError("Функция должна возвращать одно значение (градиент)")

        grad = grad[0]

        grad_x, grad_y = func(current_point[0] + step_size, current_point[1]) - func(*current_point), \
                         func(current_point[0], current_point[1] + step_size) - func(*current_point)

        if np.abs(grad_x) > np.abs(grad_y):
            next_point = current_point - np.array([grad_x, 0])
        else:
            next_point = current_point - np.array([0, grad_y])

        path.append(next_point)
        current_point = next_point

    return np.array(path)

# Визуализация рельефа и траектории спуска
def plot_terrain_and_path(x, y, z, path, start_point):
    plt.figure(figsize=(10, 8))
    plt.contourf(x, y, z, levels=50, cmap='viridis')
    plt.plot(path[:, 0], path[:, 1], 'r.-', label='Траектория спуска')
    plt.plot(start_point[0], start_point[1], 'bo', label='Начальная точка')
    plt.title('Покоординатный спуск лыжника')
    plt.xlabel('X координата')
    plt.ylabel('Y координата')
    plt.colorbar(label='Высота')
    plt.legend()
    plt.show()

# Генерация сетки значений для рельефа
x = np.linspace(-10, 10, 400)
y = np.linspace(-10, 10, 400)
x, y = np.meshgrid(x, y)
z = terrain_function(x, y)

# Начальная точка и выполнение покоординатного спуска
start_point = np.array([8, 8])
path = coordinate_descent(start_point, terrain_function)

# Визуализация
plot_terrain_and_path(x, y, z, path, start_point)
