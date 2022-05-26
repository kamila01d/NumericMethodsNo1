import numpy as np    # for compatibility with numpy in pypy
import matplotlib.pyplot as plt



N = 20
h = 1.0/N
a = np.zeros(N-1)
b = np.zeros(N)
c = np.zeros(N-1)
f = np.zeros(N)



b[0] = 1
b[N-1] = 1
f[N-1] = 1
c[0] = 0
a[N-2] = 0

for i in range(1, N-1):
    b[i] = -2 / (h*h)

for i in range(0, N-2):
    a[i] = 1 / (h**2)
for i in range(1, N-1):
    c[i] = 1 / (h**2)


def t_algorithm(a, b, c, f):
    n = len(f)
    beta = np.zeros(n - 1, float)
    gamma = np.zeros(n, float)
    x = np.zeros(n, float)

    beta[0] = (c[0] / b[0])
    gamma[0] = f[0] / b[0]

    for i in range(1, n - 1):
        beta[i] = (c[i] / (b[i] - a[i - 1] * beta[i - 1]))

    for i in range(1, n):
        gamma[i] = (f[i] - (a[i - 1] * gamma[i - 1])) / (b[i] - (a[i - 1] * beta[i - 1]))

    x[n - 1] = gamma[n - 1]

    for i in range(n - 1, 0, -1):
        x[i - 1] = gamma[i - 1] - (beta[i - 1] * x[i])

    return x


X = t_algorithm(a, b, c, f)

print(X)

plt.plot(X)
plt.show()
