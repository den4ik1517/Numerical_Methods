def f(x):
  return x**2 + x - 3

def df(x):
  return 2 * x + 1

def newton(x0, tol=1e-5, max_iter=1000):
  for _ in range(max_iter):
    x1 = x0 - f(x0) / df(x0)
    if abs(x1 - x0) < tol:
      return x1
    x0 = x1
  raise ValueError("Не знайдено кореня з заданою точністю")

x0 = -2
x = newton(x0)
print(x)
