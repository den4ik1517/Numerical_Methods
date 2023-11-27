import numpy as np
import matplotlib.pyplot as plt

R = 4
L = 0.01
C = 200
I = 100
w = 2 * np.pi * 50

def dydt(y, t):
    u1 = y[0]
    u2 = y[1]
    du1dt = -R * u1 - L * w * u2
    du2dt = -R * u2 - C * w * u1
    return np.array([du1dt, du2dt])

def explicit_euler_step(y, t, h):
    y_next = y + h * dydt(y, t)
    return y_next

y0 = np.array([0, 0])
t = np.arange(0, 0.2, 0.00001)

# Using explicit Euler method manually
y = np.zeros((len(t), len(y0)))
y[0, :] = y0

for i in range(1, len(t)):
    y[i, :] = explicit_euler_step(y[i-1, :], t[i-1], t[1] - t[0])

u2 = y[:, 1]

plt.plot(t, u2)
plt.xlabel('t')
plt.ylabel('U2')
plt.title('Transient Response of Output Voltage U2 (Explicit Euler Method)')
plt.savefig('graph3.png')
plt.show()
