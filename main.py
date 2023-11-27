import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def dydt(y, t):
    u1 = y[0]
    u2 = y[1]
    return [-R * u1 - L * w * u2, -R * u2 - C * w * u1]

def solve_ivp_implicit(f, y0, t):
    def g(y):
        return f(t, y) - y
    y = np.zeros((len(t), len(y0)))
    y[0, :] = y0

    for i in range(1, len(t)):
        # Вирішення системи неявних рівнянь
        y_next_guess = y[i-1, :] + (t[1] - t[0]) * np.array(dydt(y[i-1, :], t[i-1]))
        y[i, :] = fsolve(g, y_next_guess)

    return y

R = 4
L = 0.01
C = 200
I = 100
w = 2 * np.pi * 50

y0 = [0, 0]
t = np.arange(0, 0.2, 0.00001)

y = solve_ivp_implicit(dydt, y0, t)

u2 = y[:, 1]

plt.plot(t, u2)
plt.xlabel('t')
plt.ylabel('u2')
plt.savefig('graph.png')
plt.show()

print(y[-1, 1])
