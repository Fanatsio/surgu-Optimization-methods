import numpy as np


A = np.array([[2, 1], 
              [1, -1], 
              [0, 1]], dtype=float)
u = np.array([1, 0, 1], dtype=float)

# Вычисление транспонированной матрицы A
At = A.T

# Вычисление AtA и Atu
AtA = np.dot(At, A)
Atu = np.dot(At, u)

# Формирование расширенной матрицы системы
AugmentedMatrix = np.column_stack((AtA, Atu))

# Приведение расширенной матрицы к треугольному виду методом Гаусса
n = len(AugmentedMatrix)

for i in range(n):
    # Поиск максимального элемента в столбце i и перестановка строк
    max_row = np.argmax(np.abs(AugmentedMatrix[i:, i])) + i
    AugmentedMatrix[[i, max_row]] = AugmentedMatrix[[max_row, i]]

    # Обнуление нижележащих элементов в столбце i
    for j in range(i + 1, n):
        ratio = AugmentedMatrix[j, i] / AugmentedMatrix[i, i]
        AugmentedMatrix[j, i:] -= ratio * AugmentedMatrix[i, i:]

# Обратный ход метода Гаусса для нахождения решения
x = np.zeros(n)
for i in range(n - 1, -1, -1):
    x[i] = (AugmentedMatrix[i, -1] - np.dot(AugmentedMatrix[i, i+1:-1], x[i+1:])) / AugmentedMatrix[i, i]

print("Решение системы линейных уравнений методом Гаусса:")
print(x)
