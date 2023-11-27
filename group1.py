import numpy as np

def jacobian(f, x):
    n = len(f(x))
    df = np.zeros((n, n))
    h = 1e-8
    for i in range(n):
        x_i_plus_h = x.copy()
        x_i_plus_h[i] += h
        df[:, i] = (f(x_i_plus_h) - f(x)) / h
    return df

def newton(f, x0, tol=1e-5, max_iter=1000):
    x = np.array(x0)
    for _ in range(max_iter):
        df = jacobian(f, x)
        d, *_ = np.linalg.lstsq(df, -f(x), rcond=None)
        x = x + d
        if np.linalg.norm(d) < tol:
            return x
    raise ValueError("Не знайдено розв'язку з заданою точністю")

# Система нелінійних рівнянь
f = lambda x: np.array([x[0]**2 + x[1] - 4, x[0] + x[1]**2 - 3])

# Початкове наближення
x0 = [0.1, 0.1]

# Знаходимо розв'язки системи нелінійних рівнянь
x = newton(f, x0)

print(x)
