import numpy as np

import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 1000)

y = 3 * np.sin(x/3)

y1 = np.zeros(x.shape) + 9/(2*np.pi)
y2 = np.zeros(x.shape) + 9/(2*np.pi)
y3 = np.zeros(x.shape) + 9/(2*np.pi)


for k in range(1,3):
    y1 += (-2/np.pi)*(((-1)**k * 0.5 - 1)/(1/9 - k**2)) * np.cos(k*x)

for k in range(1,4):
    y2 += (-2/np.pi)*(((-1)**k * 0.5 - 1)/(1/9 - k**2)) * np.cos(k*x)

for k in range(1,11):
    y3 += (-2/np.pi)*(((-1)**k * 0.5 - 1)/(1/9 - k**2)) * np.cos(k*x)


plt.plot(x, y, label = 'y=3sin(3/x)')

plt.plot(x, y3, linewidth=3, label='10-я частичная сумма ряда Фурье')

plt.legend()
plt.savefig('y3.png')
plt.show()