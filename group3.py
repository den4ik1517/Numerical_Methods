def e_algorithm(A, b, x0, q, p):
  """
  Обчислює рішення системи лінійних рівнянь методом e.

  Аргументи:
    A: Матриця системи рівнянь.
    b: Вектор вільних членів.
    x0: Вектор початкових наближень.
    q: Параметр e-алгоритму.
    p: Параметр e-алгоритму.

  Повертає:
    x: Вектор рішень.
  """

  n = len(A)
  x = x0

  for i in range(n):
    x_old = x[i]
    x[i] = (x_old + q * (b[i] - sum(A[i][j] * x[j] for j in range(i)))) / (1 + q * sum(A[i][j] * A[i][j] for j in range(i)))

  for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
      x[i] -= x[j] * A[i][j] / A[i][i]

  return x

A = [[0.4, 0.3], [1.4, -0.5]]
b = [0.1, 0.1]
x0 = [0.1, 0.1]
q = 2
p = 2

x = e_algorithm(A, b, x0, q, p)

print(x)
