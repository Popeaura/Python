import matplotlib.pyplot as plt
import numpy as np

x = np.linspace (0, 10 , 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize = (8, 6))

ax1.plot(x, y1)
ax1.set_xlabel('x')
ax1.set_ylabel('sin(x)')
ax1.set_title('Line plot of sin(x)')


ax2.plot(x, y2)
ax2.set_xlabel('x')
ax2.set_ylabel('cos(x)')
ax2.set_title('Line plot of cos(x)')

plt.tight_layout()
plt.show()