import numpy as np

# Функція для визначення матриці з параметрами s та B
def create_matrix(s, B):
    A = np.array([
        [8.3, 2.62 + s, 4.1, 1.9],
        [3.92, 8.45, 7.78 - s, 2.46],
        [3.77, 7.21 + s, 8.04, 2.28],
        [2.21, 3.65 - s, 1.69, 6.69 + B]
    ])
    return A

# Функція для обчислення визначника матриці методом Гауса з вибором головного елемента по стовпцю
def determinant_gauss(matrix):
    n = len(matrix)
    det = 1

    for i in range(n):
        # Вибір головного елемента
        pivot_row = max(range(i, n), key=lambda k: abs(matrix[k, i]))
        if i != pivot_row:
            matrix[[i, pivot_row]] = matrix[[pivot_row, i]]
            det *= -1

        # Елементарні операції для зроблення нуля під головним елементом
        for j in range(i + 1, n):
            ratio = matrix[j, i] / matrix[i, i]
            matrix[j, i:] -= ratio * matrix[i, i:]

    # Обчислення визначника
    det *= np.prod(np.diagonal(matrix))
    return det

# Параметри s та B
s = 0.02 * 1  # Приклад: k = 1
B = 0.02 * 21  # Приклад: p = 21

# Створення матриці з параметрами s та B
matrix_with_params = create_matrix(s, B)

# Обчислення визначника
result = determinant_gauss(matrix_with_params)

# Вивід результату
print(f"Визначник матриці: {result}")
